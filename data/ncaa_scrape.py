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
    name = re.sub(r"\[.*?\]|\(.*?\)", "", name).lower().strip()
    return re.sub(r"[^a-z0-9]", "", name)


def normalize_url(url: str) -> str:
    if not isinstance(url, str):
        return ""
    url = url.lower().strip()
    url = re.sub(r"https?://", "", url)
    url = re.sub(r"^www\.", "", url)
    domain = url.split("/")[0]

    parts = domain.split(".")
    if len(parts) > 2:
        domain = ".".join(parts[-2:])
    return domain


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
            }
        )
    return pd.DataFrame(schools)


def get_ncaa_data():
    df = pd.concat([fetch_ncaa_division(d) for d in range(1, 4)], ignore_index=True)
    df["lookup"] = df["school"].apply(normalize_name)
    return df


def load_ipeds_windows(accdb_path, hd, ic):
    try:
        import pyodbc

        conn_str = (
            f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={accdb_path};"
        )
        conn = pyodbc.connect(conn_str)

        query_ic = f"SELECT UNITID, ASSOC1 FROM {ic.replace('.csv', '')}"
        query_hd = f"SELECT UNITID, INSTNM, WEBADDR FROM {hd.replace('.csv', '')}"

        df_ic = pd.read_sql(query_ic, conn, dtype={"UNITID": str})
        df_hd = pd.read_sql(query_hd, conn, dtype={"UNITID": str})

        conn.close()

        df = df_ic.merge(df_hd, on="UNITID", how="left")
        df["lookup"] = df["INSTNM"].apply(normalize_name)
        df["url_lookup"] = df["WEBADDR"].apply(normalize_url)

        return df[["UNITID", "INSTNM", "lookup", "url_lookup", "ASSOC1"]]

    except (ImportError, Exception) as e:
        print(f"Windows ACCDB connection failed: {e}")
        return None


def load_ipeds_mac(accdb_path, hd, ic):
    try:
        subprocess.run(["which", "mdb-export"], check=True, capture_output=True)

        with tempfile.TemporaryDirectory() as temp_dir:
            ic_csv = os.path.join(temp_dir, ic)
            hd_csv = os.path.join(temp_dir, hd)

            with open(ic_csv, "w") as f:
                subprocess.run(
                    ["mdb-export", accdb_path, ic.replace("csv", "")],
                    stdout=f,
                    check=True,
                )

            with open(hd_csv, "w") as f:
                subprocess.run(
                    ["mdb-export", accdb_path, hd.replace("csv", "")],
                    stdout=f,
                    check=True,
                )

            df_ic = pd.read_csv(ic_csv, dtype={"UNITID": str})
            df_hd = pd.read_csv(hd_csv, dtype={"UNITID": str})

            df = df_ic.merge(
                df_hd[["UNITID", "INSTNM", "WEBADDR"]], on="UNITID", how="left"
            )
            df["lookup"] = df["INSTNM"].apply(normalize_name)
            df["url_lookup"] = df["WEBADDR"].apply(normalize_url)

            return df[["UNITID", "INSTNM", "lookup", "url_lookup", "ASSOC1"]]

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Mac mdb-tools failed: {e}")
        return None


def load_ipeds_csv(ic, hd):
    try:
        df_ic = pd.read_csv(ic, encoding="latin1", dtype={"UNITID": str}).rename(
            columns={"UNITID": "UNITID"}
        )
        df_hd = pd.read_csv(hd, encoding="latin1", dtype={"UNITID": str}).rename(
            columns={"UNITID": "UNITID", "INSTNM": "INSTNM"}
        )
        df = df_ic.merge(
            df_hd[["UNITID", "INSTNM", "WEBADDR"]], on="UNITID", how="left"
        )
        df["lookup"] = df["INSTNM"].apply(normalize_name)
        df["url_lookup"] = df["WEBADDR"].apply(normalize_url)
        return df[["UNITID", "INSTNM", "lookup", "url_lookup", "ASSOC1"]]
    except Exception as e:
        print(f"CSV loading failed: {e}")
        raise


def load_ipeds(accdb_path, ic, hd):
    if os.path.exists(accdb_path):
        print(f"Found ACCDB file: {accdb_path}")

        if platform.system() == "Windows":
            print("Using Windows pyodbc method...")
            df = load_ipeds_windows(accdb_path, ic, hd)
            if df is not None:
                print("Successfully loaded from ACCDB on Windows")
                return df

        else:
            print("Using non-windows mdb-tools method...")
            df = load_ipeds_mac(accdb_path, ic, hd)
            if df is not None:
                print("Successfully loaded from ACCDB on non-Windows")
                return df

    print("Falling back to CSV files...")
    if os.path.exists(ic) and os.path.exists(hd):
        print(f"Loading from CSV files: {ic}, {hd}")
        return load_ipeds_csv(ic, hd)
    else:
        print(f"CSV files not found: {ic}, {hd}")
        raise FileNotFoundError("Neither ACCDB nor CSV files found")


def merge_ncaa_ipeds(df_ncaa, df_ipeds):
    merged = df_ncaa.merge(df_ipeds, on="lookup", how="left", suffixes=("", "_ipeds"))
    initial_name_matches = merged["UNITID"].notna().sum()
    print(f"Name matches: {initial_name_matches}")

    missing_url = merged[merged["UNITID"].isna()]
    url_matches = 0
    if not missing_url.empty:
        print(f"Trying URL matching for {len(missing_url)} schools...")
        for idx, row in missing_url.iterrows():
            if row["school_url"]:
                match = df_ipeds[df_ipeds["url_lookup"] == row["school_url"]]
                if not match.empty:
                    merged.at[idx, "UNITID"] = match.iloc[0]["UNITID"]
                    merged.at[idx, "match_method"] = "URL"
                    url_matches += 1
        print(f"URL matches: {url_matches}")

    still_missing = merged[merged["UNITID"].isna()]["school"].unique()
    fuzzy_matches = 0
    unmatched = []
    if len(still_missing) > 0:
        print(f"{len(still_missing)} schools unmatched, trying fuzzy matching...")
        ipeds_names = df_ipeds["lookup"].tolist()
        for school in still_missing:
            best, score = process.extractOne(normalize_name(school), ipeds_names)
            if score >= 90:
                matched_unitid = df_ipeds[df_ipeds["lookup"] == best]["UNITID"].values[
                    0
                ]
                merged.loc[merged["school"] == school, "UNITID"] = matched_unitid
                merged.loc[merged["school"] == school, "match_method"] = "Fuzzy"
                fuzzy_matches += 1
            else:
                unmatched.append(school)
        print(f"Fuzzy matches: {fuzzy_matches}")

    if unmatched:
        pd.DataFrame({"unmatched_school": unmatched}).to_csv(
            "unmatched_schools.csv", index=False
        )
        print(f"Saved {len(unmatched)} unmatched schools to unmatched_schools.csv")

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
    ACCDB_PATH = "data/IPEDS202324.accdb"
    IC_PATH = "data/IC2023.csv"
    HD_PATH = "data/HD2023.csv"

    df_ncaa = get_ncaa_data()
    df_ipeds = load_ipeds(accdb_path=ACCDB_PATH, ic=IC_PATH, hd=HD_PATH)
    df_merged = merge_ncaa_ipeds(df_ncaa, df_ipeds)
    final = build_division_mapping(df_merged, df_ipeds)
    final.to_csv("data/ncaa_divisions.csv", index=False)
    print(f"Saved {len(final)} rows to data/ncaa_divisions.csv")


if __name__ == "__main__":
    main()
