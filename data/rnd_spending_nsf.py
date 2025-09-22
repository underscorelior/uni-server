# CONVERTS TABLE 22 OF THE NSF HERD REPORT TO CSV TO BE USED IN DB
import platform
import pandas as pd
from thefuzz import process
import re
import os
import subprocess
import tempfile


def normalize(name: str) -> str:
    if not isinstance(name, str):
        return ""
    return re.sub(
        r"[^a-z0-9]",
        "",
        re.sub(
            r"\[.*?\]|\(.*?\)",
            "",
            name.replace("U.", "university")
            .replace("C.", "college")
            .replace("of ", "")
            .replace(" of", "")
            .replace("&", "and")
            .replace(" at ", " ")
            .replace("The ", ""),
        ).lower(),
    )


def _finalize(df_hd: pd.DataFrame) -> pd.DataFrame:
    df = df_hd.copy()
    df["lookup"] = df["INSTNM"].apply(normalize)
    return df[["UNITID", "INSTNM", "lookup"]]


def _load_windows(accdb_path, hd):
    import pyodbc

    conn = pyodbc.connect(
        f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={os.getcwd()}/{accdb_path};"
    )
    df_hd = pd.read_sql(
        f"SELECT UNITID, INSTNM FROM {hd}",
        conn,
        dtype={"UNITID": str},
    )
    conn.close()
    return _finalize(df_hd)


def _load_mac(accdb_path, hd):
    subprocess.run(["which", "mdb-export"], check=True, capture_output=True)
    with tempfile.TemporaryDirectory() as tmp:
        hd_csv = os.path.join(tmp, hd + ".csv")
        with open(hd_csv, "w") as f:
            subprocess.run(
                ["mdb-export", accdb_path, hd],
                stdout=f,
                check=True,
            )

        df_hd = pd.read_csv(hd_csv, dtype={"UNITID": str})
    return _finalize(df_hd)


def load_ipeds(accdb_path, hd):
    if os.path.exists(accdb_path):
        try:
            if platform.system() == "Windows":
                return _load_windows(accdb_path, hd)
            else:
                return _load_mac(accdb_path, hd)
        except Exception:
            pass

    raise FileNotFoundError("ACCDB file not found")


def load_spending(EXCEL_PATH):
    df = pd.read_excel(EXCEL_PATH)
    df.drop(range(0, 5), inplace=True)
    df.rename(
        {"Table 22": "inst", "Unnamed: 2": "rnd"},
        axis=1,
        inplace=True,
    )

    return df[["inst", "rnd"]]


def main():
    EXCEL_PATH = "data/sources/nsf25314-tab022.xlsx"
    ACCDB_PATH = "data/sources/IPEDS202324.accdb"
    HD_TBL = "HD2023"

    HARDCODED_FIXES = {
        "Georgia Institute": "139755",
        "Hershey Medical Center": "214777",
        "New Brunswick": "186380",
        "West Lafayette": "243780",
        "Charlottesville": "234076",
        "Buffalo": "196088",
        "Baton Rouge": "159391",
        "Auburn University": "100858",
        "Albany": "196060",
        "Oklahoma, Norman": "207342",
        "Montana, Missoula": "180489",
        "New Jersey, Camden": "186371",
        "Bozeman": "180461",
        "New Mexico State": "188030",
        "Bowling Green State": "201441",
        "Brockport": "196121",
        "SUNY, Geneseo": "196167",
        "Staten Island": "190558",
        "Touro": "196592",
        "Missouri State": "179566",
        "Harrisburg": "214713",
        "North Texas, Denton": "227216",
        "Florida A&M": "133650",
        "Pratt Institute": "194578",
        "Wright State": "206604",
        "New Jersey, Newark": "186399",
        "Altoona": "214689",
        "SUNY, Oswego": "196194",
        "Ana G. Mendez, Gurabo": "243601",
        "SUNY, Cobleskill": "196033",
        "CUNY, Baruch": "190512",
        "Indiana U. Pennsylvania": "213020",
        "Embry-Riddle Aeronautical": "133553",
        "Behrend": "214591",
        "U. Texas Medical Branch": "228653",
        "Oklahoma State U., Stillwater": "207388",
        "CUNY, Graduate Center": "190576",
        "U.S. Air Force Academy": "128328",
        "U.S. Military Academy": "197036",
        "U.S. Naval Academy": "164155",
        "William Paterson U.": "187444",
        "High Tech High Graduate School of Ed.": "485403",
        "Palmer C. of Chiropractic": "154174",
        "U.S. Coast Guard Academy": "130624",
    }

    df_spend = load_spending(EXCEL_PATH)
    df_ipeds = load_ipeds(ACCDB_PATH, HD_TBL)
    df_spend["lookup"] = df_spend["inst"].apply(normalize)
    df_merged = df_spend.merge(
        df_ipeds, on="lookup", how="left", suffixes=("", "_ipeds")
    )
    unmatched = df_merged[df_merged["UNITID"].isna()]["inst"].unique()
    print(f"{len(unmatched)} schools unmatched, trying fuzzy matching...")
    ipeds_names = df_ipeds["lookup"].tolist()
    fuzzy_matches = 0
    for school in unmatched:
        best, score = process.extractOne(normalize(school), ipeds_names)
        if score >= 90:
            uid = df_ipeds[df_ipeds["lookup"] == best]["UNITID"].values[0]
            df_merged.loc[df_merged["inst"] == school, ["UNITID"]] = [
                uid,
            ]
            fuzzy_matches += 1
        for k, v in HARDCODED_FIXES.items():
            if normalize(k) in normalize(school):
                df_merged.loc[df_merged["inst"] == school, ["UNITID"]] = [v]

    print(f"Fuzzy matches: {fuzzy_matches}")
    unmatched = df_merged[df_merged["UNITID"].isna()]["inst"].unique()
    df_merged = df_merged[~df_merged["UNITID"].isna()]
    if len(unmatched) > 0:
        print(f"Unmatched schools: {unmatched}")
    df_new = df_merged[["UNITID", "rnd"]]
    df_new.to_csv("data/out/rnd_spending.csv", index=False)


if __name__ == "__main__":
    main()
