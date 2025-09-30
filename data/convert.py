import os
import pandas as pd
import subprocess
import tempfile
from sqlalchemy import create_engine
from data import schema, data
from score import scoring_components
from gen_aliases import aliases
import platform
import sqlite3
from rich import print
import re

if platform.system() == "Windows":
    import pyodbc


def compute_endowment_fte(row):
    control = row.get("CNTLAFFI", -1)
    if control == 1:
        if pd.notnull(row.get("F1ENDMFT")):
            return row.get("F1ENDMFT")
        if (
            pd.notnull(row.get("F1CORREV"))
            and pd.notnull(row.get("FTE12MN"))
            and row.get("FTE12MN", 0) != 0
        ):
            return round(row["F1CORREV"] / row["FTE12MN"])
        return None
    elif control in [3, 4]:
        if pd.notnull(row.get("F2ENDMFT")):
            return row.get("F2ENDMFT")
        if (
            pd.notnull(row.get("F2CORREV"))
            and pd.notnull(row.get("FTE12MN"))
            and row.get("FTE12MN", 0) != 0
        ):
            return round(row["F2CORREV"] / row["FTE12MN"])
        return None

    elif control == 2:
        if (
            pd.notnull(row.get("F3CORREV"))
            and pd.notnull(row.get("FTE12MN"))
            and row.get("FTE12MN", 0) != 0
        ):
            return round(row["F3CORREV"] / row["FTE12MN"])
        if pd.notnull(row.get("F3A01")) and pd.notnull(row.get("FTE12MN")):
            return round(row["F3A01"] / row["FTE12MN"])
        return None
    else:
        return None


def get_access_table_data(access_db_path, table_name, columns):
    if platform.system() == "Windows":
        try:
            conn_str = (
                r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                f"DBQ={os.path.abspath(access_db_path)};"
            )
            with pyodbc.connect(conn_str) as conn:
                query = f"SELECT {', '.join(columns)} FROM {table_name}"
                df = pd.read_sql(query, conn)
            return df
        except Exception as e:
            print(f"Error reading table {table_name} via pyodbc: {e}")
            return None
    else:
        try:
            cmd = ["mdb-export", access_db_path, table_name]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".csv", delete=False
            ) as temp_file:
                temp_file.write(result.stdout)
                temp_csv_path = temp_file.name

            df = pd.read_csv(temp_csv_path)
            os.unlink(temp_csv_path)

            available_columns = [col for col in columns if col in df.columns]
            if available_columns:
                return df[available_columns]
            else:
                print(
                    f"[bold orange]Warning:[/bold orange] None of the requested columns found in table {table_name}"
                )
                return df
        except subprocess.CalledProcessError as e:
            print(f"Error exporting table {table_name}: {e}")
            print(f"stderr: {e.stderr}")
            return None
        except Exception as e:
            print(f"Error processing table {table_name}: {e}")
            return None


def apply_special_cases(df, div_path, found_csv, rnd_path, cpf_path, column_rename_map):
    if "DIV_DIV" in column_rename_map:
        if not os.path.exists(div_path):
            print(
                f"[bold orange]Warning:[/bold orange] Division CSV '{div_path}' not found."
            )
        else:
            div_df = pd.read_csv(div_path)
            df = pd.merge(df, div_df, on="UNITID", how="left")
            df.rename(columns={"div": "DIV_DIV"}, inplace=True)

    if "YEAR" in column_rename_map:
        if not os.path.exists(found_csv):
            print(
                f"[bold orange]Warning:[/bold orange] Founding year CSV '{found_csv}' not found."
            )
        else:
            div_df = pd.read_csv(found_csv)
            df = pd.merge(df, div_df, on="UNITID", how="left")
            df.rename(columns={"foundyr": "YEAR"}, inplace=True)

    if "RND_SPEND" in column_rename_map:
        if not os.path.exists(rnd_path):
            print(
                f"[bold orange]Warning:[/bold orange] RnD CSV '{rnd_path}' not found."
            )
        else:
            rnd_df = pd.read_csv(rnd_path)
            df = pd.merge(df, rnd_df, on="UNITID", how="left")
            df.rename(columns={"rnd": "RND_SPEND"}, inplace=True)

    if "QS_CPF" in column_rename_map:
        if not os.path.exists(cpf_path):
            print(
                f"[bold orange]Warning:[/bold orange] QS Citations CSV '{cpf_path}' not found."
            )
        else:
            cpf_df = pd.read_csv(cpf_path)
            cpf_df.rename(columns={"cpf": "QS_CPF"}, inplace=True)
            df = pd.merge(df, cpf_df[["UNITID", "QS_CPF"]], on="UNITID", how="left")

    if "GALIAS" in column_rename_map:
        df["GALIAS"] = df.apply(
            lambda row: ", ".join(
                aliases(row["INSTNM"], row.get("F1SYSNAM", ""), row.get("WEBADDR", ""))
            ),
            axis=1,
        )

    if "ENDOW_FTE" in column_rename_map:
        if all(
            col in df.columns
            for col in [
                "CNTLAFFI",
                "F1ENDMFT",
                "F2ENDMFT",
                "F3CORREV",
                "FTE12MN",
                "F1CORREV",
                "F2CORREV",
                "F3A01",
            ]
        ):
            df["ENDOW_FTE"] = df.apply(compute_endowment_fte, axis=1)

        else:
            missing_cols = [
                col
                for col in [
                    "CNTLAFFI",
                    "F1ENDMFT",
                    "F2ENDMFT",
                    "F3CORREV",
                    "FTE12MN",
                    "F1CORREV",
                    "F2CORREV",
                    "F3A01",
                ]
                if col not in df.columns
            ]
            df["ENDOW_FTE"] = None
            print(
                f"[bold orange]Warning:[/bold orange] Cannot compute 'ENDOW_FTE' as required columns are missing: {missing_cols}"
            )

    for col in list(column_rename_map.keys()):
        if col.endswith("_DUP"):
            original_col = col[:-4]
            if original_col in df.columns:
                df[col] = df[original_col]
                print(f"Created '{col}' as a duplicate of '{original_col}'")
            else:
                print(
                    f"[bold orange]Warning:[/bold orange] Cannot create '{col}' because '{original_col}' is missing."
                )

    if "GENTELE" in df.columns:

        def clean_phone(x):
            if pd.isnull(x):
                return None
            x = re.sub("[^0-9]", "", x)
            return x if len(str(x)) == 10 else None

        df["GENTELE"] = df["GENTELE"].apply(clean_phone)

    pct_columns = [
        col
        for col in column_rename_map.values()
        if col.lower().startswith("pct_")
        or col.lower().endswith("_pct")
        or "_rate" in col.lower()
    ]
    print("PCT columns from rename map values:", pct_columns)
    for col in pct_columns:
        original_col = next((k for k, v in column_rename_map.items() if v == col), None)
        if (
            original_col
            and original_col in df.columns
            and df[original_col].dtype in [float, int]
        ):
            if (df[original_col] > 1).any():
                df[original_col] = df[original_col] / 100.0
            else:
                print(f"'{col}' already has values less than or equal to 1.")

    if "PCTE12DEEXC" in df.columns:
        df["ONLINE"] = df["PCTE12DEEXC"].apply(
            lambda x: 1 if pd.notnull(x) and x > 0.5 else (2 if pd.notnull(x) else -1)
        )
    return df


def create_search_view(SQLITE_PATH):
    conn = sqlite3.connect(SQLITE_PATH)
    conn.execute(
        """
        CREATE VIEW IF NOT EXISTS search AS
        SELECT
            core.ID,
            core.NAME,
            core.ALIAS,
            core.GEN_ALIAS,
            core.CITY,
            core.STATE,
            enrollment.FT_POP AS FULL_TIME,
            enrollment.PT_POP AS PART_TIME,
            enrollment.ONLINE
        FROM
            core, enrollment
        WHERE
            core.ID = enrollment.ID;
        """
    )
    conn.commit()
    conn.close()


def create_list_view(SQLITE_PATH):
    conn = sqlite3.connect(SQLITE_PATH)
    conn.execute(
        """
        CREATE VIEW IF NOT EXISTS list AS
        SELECT
            core.ID,
            core.NAME,
            core.URL,
            core.CITY,
            core.STATE,
            core.YEAR,
            core.INST_CONTROL,
            core.SCORE,
            enrollment.FTE_POP,
            admissions.ACC_RATE
        FROM
            core
        JOIN enrollment ON core.ID = enrollment.ID
        JOIN admissions ON core.ID = admissions.ID;
        """
    )
    conn.commit()
    conn.close()


def create_descriptions_table(SQLITE_PATH):
    conn = sqlite3.connect(SQLITE_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS descriptions (
            id INTEGER UNIQUE,
            description TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def add_score_column(SQLITE_PATH):
    conn = sqlite3.connect(SQLITE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 
            core.ID, 
            core.ENDOW_FTE, 
            enrollment.FTE_POP, 
            enrollment.FT_POP, 
            enrollment.PT_POP, 
            admissions.APPL_TOTAL, 
            admissions.ACC_RATE,
            admissions.YIELD_RATE, 
            outcomes.GRAD_RATE_6_YR, 
            outcomes.RET_RATE_FT, 
            outcomes.RET_RATE_PT, 
            core.RND_SPEND,
            core.CRN_BASIC, 
            core.QS_CPF,
            enrollment.ONLINE
        FROM core
        JOIN enrollment ON core.ID = enrollment.ID 
        JOIN admissions ON core.ID = admissions.ID
        JOIN outcomes ON core.ID = outcomes.ID
        """
    )
    rows = cursor.fetchall()

    df = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "ENDOW_FTE",
            "FTE_POP",
            "FT_POP",
            "PT_POP",
            "APPL_TOTAL",
            "ACC_RATE",
            "YIELD_RATE",
            "GRAD_RATE_6_YR",
            "RET_RATE_FT",
            "RET_RATE_PT",
            "RND_SPEND",
            "CRN_BASIC",
            "QS_CPF",
            "ONLINE",
        ],
    )
    df = df.fillna(0)
    df.insert(0, "SCORE", 0)

    df["SCORE"] = df.apply(lambda r: scoring_components(r, df), axis=1)
    df["SCORE"] = df["SCORE"].apply(lambda c: sum(c.values()))

    cursor.execute("ALTER TABLE core ADD COLUMN SCORE REAL")
    for _, row in df.iterrows():
        cursor.execute(
            "UPDATE core SET SCORE = ? WHERE ID = ?", (row["SCORE"], row["ID"])
        )
    conn.commit()
    conn.close()

    print(df.head(15))


def get_source_table_for_col(column_name, schema):
    for table, columns in schema.items():
        if column_name in columns:
            return table
    return None


def main():
    ACCESS_DB_PATH = "data/sources/IPEDS202324.accdb"
    SQL_OUTPUT_PATH = "data/universities.sqlite"
    DESCRIPTIONS_CSV_PATH = "data/out/descriptions.csv"
    DIVISION_CSV = "data/out/ncaa_divisions.csv"
    RND_CSV = "data/out/rnd_spending.csv"
    CPF_CSV = "data/out/qs_citations.csv"
    FOUND_CSV = "data/out/founding.csv"

    if not os.path.exists(ACCESS_DB_PATH):
        print(
            f"[red bold]Error[/red bold]: Access database not found at '{ACCESS_DB_PATH}'"
        )
        return

    if os.path.exists(SQL_OUTPUT_PATH):
        conn = sqlite3.connect(SQL_OUTPUT_PATH)
        try:
            df = pd.read_sql("SELECT * FROM descriptions", conn)
            df.to_csv(DESCRIPTIONS_CSV_PATH, index=False)
            print(f"Saved existing descriptions to '{DESCRIPTIONS_CSV_PATH}'")
        except Exception as _:
            print("Descriptions not found")
            open(DESCRIPTIONS_CSV_PATH)
        conn.close()

    os.makedirs(os.path.dirname(SQL_OUTPUT_PATH), exist_ok=True)
    if os.path.exists(SQL_OUTPUT_PATH):
        os.remove(SQL_OUTPUT_PATH)
    engine = create_engine(f"sqlite:///{SQL_OUTPUT_PATH}")

    filter_columns = [
        "ICLEVEL",
        "SECTOR",
        "DEATHYR",
        "CYACTIVE",
        "DEGGRANT",
        "INSTSIZE",
        "POSTSEC",
    ]

    for tn, rnmp in schema.items():
        print(f"\nProcessing table: {tn}")
        source_cols_for_this_table = list(rnmp.keys())
        source_tables_to_query = {}

        for col in source_cols_for_this_table:
            source_table = get_source_table_for_col(col, data)
            if source_table:
                source_tables_to_query.setdefault(source_table, set()).add(col)

        if "ENDOW_FTE" in rnmp:
            source_tables_to_query.setdefault("DRVF2023", set()).update(
                ["F1ENDMFT", "F1CORREV", "F2ENDMFT", "F2CORREV", "F3CORREV"]
            )

            source_tables_to_query.setdefault("F2223_F3", set()).add("F3A01")
            source_tables_to_query.setdefault("DRVEF122023", set()).add("FTE12MN")

        # TODO: Maybe save ID of all filtered colleges to prevent recalling this
        if "HD2023" not in source_tables_to_query:
            source_tables_to_query["HD2023"] = set()
        source_tables_to_query["HD2023"].update(filter_columns)

        if not source_tables_to_query:
            print(f"Skipping table '{tn}' as no source columns were found.")
            continue

        dataframes = {}
        for table_name, columns in source_tables_to_query.items():
            columns.add("UNITID")
            print(f"  Querying source table '{table_name}'...")
            df = get_access_table_data(ACCESS_DB_PATH, table_name, columns)
            if df is not None:
                dataframes[table_name] = df
            else:
                print(f"  ERROR reading table '{table_name}'")

        if "HD2023" not in dataframes:
            print("  ERROR: 'HD2023' was not loaded.")
            continue

        merged_df = dataframes.pop("HD2023")
        for df in dataframes.values():
            merged_df = pd.merge(merged_df, df, on="UNITID", how="left")

        initial_rows = len(merged_df)
        filtered_df = merged_df[
            (merged_df["ICLEVEL"].isin([1, 2]))
            & (merged_df["SECTOR"] != 0)
            & (merged_df["DEATHYR"] == -2)
            & (merged_df["CYACTIVE"] == 1)
            & (merged_df["DEGGRANT"] == 1)
            & (merged_df["INSTSIZE"] > 0)
            & (merged_df["POSTSEC"] == 1)
        ].copy()
        print(f"  Filtered {initial_rows} records down to {len(filtered_df)}.")

        filtered_df = apply_special_cases(
            filtered_df, DIVISION_CSV, FOUND_CSV, RND_CSV, CPF_CSV, rnmp
        )

        final_cols_original_names = [
            col for col in rnmp.keys() if col in filtered_df.columns
        ]
        if "UNITID" not in final_cols_original_names:
            final_cols_original_names.insert(0, "UNITID")
        if (
            "ONLINE" in filtered_df.columns
            and "ONLINE" not in final_cols_original_names
        ):
            final_cols_original_names.append("ONLINE")

        new_table_df = filtered_df[final_cols_original_names].copy()
        new_table_df.rename(columns=rnmp, inplace=True)

        new_table_df.to_sql(tn, engine, if_exists="replace", index=False)
        print(f"  Exported '{tn}' - {len(new_table_df.columns)} columns.")

    print(f"\nSuccess! All tables exported to '{SQL_OUTPUT_PATH}'")

    print("\nCreating 'search' and 'list' views...")
    create_search_view(SQL_OUTPUT_PATH)
    print("Created 'search' view successfully.")
    create_list_view(SQL_OUTPUT_PATH)
    print("Created 'list' view successfully.")

    print("\nCreating 'descriptions' table...")
    create_descriptions_table(SQL_OUTPUT_PATH)

    print("\nScoring colleges...")
    add_score_column(SQL_OUTPUT_PATH)

    if os.path.exists(DESCRIPTIONS_CSV_PATH):
        descriptions_df = pd.read_csv(DESCRIPTIONS_CSV_PATH, dtype={"UNITID": str})
        descriptions_df.to_sql("descriptions", engine, if_exists="replace", index=False)
        os.remove(DESCRIPTIONS_CSV_PATH)
        print(f"Descriptions imported from '{DESCRIPTIONS_CSV_PATH}'")

    else:
        print(
            f"[bold orange]Warning:[/bold orange] Descriptions CSV '{DESCRIPTIONS_CSV_PATH}' not found."
        )


if __name__ == "__main__":
    main()
