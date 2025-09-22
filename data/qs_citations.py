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
        re.sub(r"\[.*?\]|\(.*?\)", "", name).lower(),
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


def load_citations(QS_FILE):
    df = pd.read_csv(QS_FILE, sep="\t", header=0)
    print(df.head(5))
    df.rename(
        {"Name": "inst", "Citations per Faculty SCORE": "cpf"},
        axis=1,
        inplace=True,
    )

    return df[["inst", "cpf"]]


def main():
    QS_FILE = "data/sources/qs.tsv"
    ACCDB_PATH = "data/sources/IPEDS202324.accdb"
    HD_TBL = "HD2023"

    HARDCODED_FIXES = {
        "The City College of New York": "190567",
        "Georgia Institute of Technology": "139755",
        "City University of New York": "190512",
        "IU Indianapolis": "151111",
        "California Polytechnic State University": "110422",
        "New Mexico State University": "188030",
        "Pratt Institute": "194578",
        "University of Minnesota (System)": "174066",
    }
    df_cpf = load_citations(QS_FILE)
    df_ipeds = load_ipeds(ACCDB_PATH, HD_TBL)
    df_cpf["lookup"] = df_cpf["inst"].apply(normalize)
    df_merged = df_cpf.merge(df_ipeds, on="lookup", how="left", suffixes=("", "_ipeds"))
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
    df_new = df_merged[["UNITID", "cpf"]]
    df_new.to_csv("data/out/qs_citations.csv", index=False)


if __name__ == "__main__":
    main()
