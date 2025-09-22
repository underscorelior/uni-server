import requests
import pandas as pd
import re
from thefuzz import process
import os
import platform
import subprocess
import tempfile


def normalize_name(name: str) -> str:
    if not isinstance(name, str):
        return ""
    return re.sub(
        r"[^a-z0-9]",
        "",
        re.sub(r"\[.*?\]|\(.*?\)", "", name).lower(),
    )


def normalize_url(url: str) -> str:
    if not isinstance(url, str):
        return ""
    url = re.sub(r"https?://|^www\\.", "", url.lower().strip()).split("/")[0]
    parts = url.split(".")
    return ".".join(parts[-2:]) if len(parts) > 2 else url


def fetch_ncaa_division(division: int):
    url = f"https://web3.ncaa.org/directory/api/directory/memberList?type=12&division={division*"I"}"
    print(f"Fetching NCAA Division {division} data...")
    data = requests.get(url).json()
    schools = []
    for entry in data:
        school_url = entry.get("webSiteUrl") or entry.get("webSite", "")
        schools.append(
            {
                "school": entry["nameOfficial"],
                "div": division,
                "school_url": normalize_url(school_url),
                "match_method": "Name",
                "lookup": normalize_name(entry["nameOfficial"]),
            }
        )
    return pd.DataFrame(schools)


def get_ncaa_data():
    return pd.concat([fetch_ncaa_division(d) for d in range(1, 4)], ignore_index=True)


def _finalize(df_ic: pd.DataFrame, df_hd: pd.DataFrame) -> pd.DataFrame:
    df = df_ic.merge(df_hd[["UNITID", "INSTNM", "WEBADDR"]], on="UNITID", how="left")
    df["lookup"] = df["INSTNM"].apply(normalize_name)
    df["url_lookup"] = df["WEBADDR"].apply(normalize_url)
    return df[["UNITID", "INSTNM", "lookup", "url_lookup", "ASSOC1"]]


def _load_windows(accdb_path, ic, hd):
    import pyodbc

    conn = pyodbc.connect(
        f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={os.getcwd()}/{accdb_path};"
    )
    df_ic = pd.read_sql(f"SELECT UNITID, ASSOC1 FROM {ic}", conn, dtype={"UNITID": str})
    df_hd = pd.read_sql(
        f"SELECT UNITID, INSTNM, WEBADDR FROM {hd}", conn, dtype={"UNITID": str}
    )
    conn.close()
    return _finalize(df_ic, df_hd)


def _load_mac(accdb_path, ic, hd):
    subprocess.run(["which", "mdb-export"], check=True, capture_output=True)
    with tempfile.TemporaryDirectory() as tmp:
        ic_csv = os.path.join(tmp, ic + ".csv")
        hd_csv = os.path.join(tmp, hd + ".csv")
        for tbl, out in [(ic, ic_csv), (hd, hd_csv)]:
            with open(out, "w") as f:
                print(f"Running mdb-export for {tbl}...")
                subprocess.run(
                    ["mdb-export", accdb_path, tbl],
                    stdout=f,
                    check=True,
                )

        df_ic = pd.read_csv(ic_csv, dtype={"UNITID": str})
        df_hd = pd.read_csv(hd_csv, dtype={"UNITID": str})
    return _finalize(df_ic, df_hd)


def load_ipeds(accdb_path, ic, hd):
    if os.path.exists(accdb_path):
        try:
            if platform.system() == "Windows":
                return _load_windows(accdb_path, ic, hd)
            else:
                return _load_mac(accdb_path, ic, hd)
        except Exception:
            pass
    raise FileNotFoundError("ACCDB file not found")


def merge_ncaa_ipeds(df_ncaa, df_ipeds):
    merged = df_ncaa.merge(df_ipeds, on="lookup", how="left", suffixes=("", "_ipeds"))

    initial_name_matches = merged["UNITID"].notna().sum()
    print(f"Name matches: {initial_name_matches}")

    assigned = set(merged[merged["UNITID"].notna()]["UNITID"])

    missing = merged[merged["UNITID"].isna()]
    url_matches = 0
    print(f"Trying URL matching for {len(missing)} schools...")
    for idx, row in missing.iterrows():
        if row["school_url"]:
            match = df_ipeds[df_ipeds["url_lookup"] == row["school_url"]]
            if not match.empty:
                uid = match.iloc[0]["UNITID"]
                if uid not in assigned:
                    merged.at[idx, "UNITID"] = uid
                    merged.at[idx, "match_method"] = "URL"
                    assigned.add(uid)
                    url_matches += 1
    print(f"URL matches: {url_matches}")

    miss = merged[merged["UNITID"].isna()]["school"].unique()
    fuzzy_matches = 0
    unmatched = []
    print(f"{len(miss)} schools unmatched, trying fuzzy matching...")
    ipeds_names = df_ipeds["lookup"].tolist()
    for school in miss:
        best, score = process.extractOne(normalize_name(school), ipeds_names)
        if score >= 90:
            uid = df_ipeds[df_ipeds["lookup"] == best]["UNITID"].values[0]
            if uid not in assigned:
                merged.loc[merged["school"] == school, ["UNITID", "match_method"]] = [
                    uid,
                    "Fuzzy",
                ]
                assigned.add(uid)
                fuzzy_matches += 1
        else:
            unmatched.append(school)
    print(f"Fuzzy matches: {fuzzy_matches}")

    if unmatched:
        pd.DataFrame({"unmatched_school": unmatched}).to_csv(
            "unmatched_schools.csv", index=False
        )
        print(f"Saved {len(unmatched)} unmatched schools to unmatched_schools.csv")

    final_matched = merged[merged["UNITID"].notna()]
    final_matched[final_matched.duplicated(subset=["UNITID"], keep=False)]

    print(
        f"Matching stats -> Name: {initial_name_matches}, URL: {url_matches}, Fuzzy: {fuzzy_matches}, Unmatched: {len(unmatched)}"
    )
    return merged


def build_division_mapping(df_merged, df_ipeds):
    df = df_ipeds.merge(df_merged[["UNITID", "div"]], on="UNITID", how="left")
    df["div"] = df.apply(
        lambda x: (int(x["div"]) if pd.notna(x["div"]) and x["ASSOC1"] == 1 else 0),
        axis=1,
    )
    return df[["UNITID", "div"]].astype(int)


def main():
    ACCDB_PATH = "data/sources/IPEDS202324.accdb"
    IC_TBL = "IC2023"
    HD_TBL = "HD2023"

    df_ncaa = get_ncaa_data()
    df_ipeds = load_ipeds(accdb_path=ACCDB_PATH, ic=IC_TBL, hd=HD_TBL)
    df_merged = merge_ncaa_ipeds(df_ncaa, df_ipeds)
    final = build_division_mapping(df_merged, df_ipeds)
    final.to_csv("data/out/ncaa_divisions.csv", index=False)
    print(f"Saved {len(final)} rows to data/out/ncaa_divisions.csv")


if __name__ == "__main__":
    main()
