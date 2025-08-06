import os
import pandas as pd
import subprocess
import tempfile
from sqlalchemy import create_engine
from data import schema, data
import platform
import pyodbc
import sqlite3


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
                    f"Warning: None of the requested columns found in table {table_name}"
                )
                return df
        except subprocess.CalledProcessError as e:
            print(f"Error exporting table {table_name}: {e}")
            print(f"stderr: {e.stderr}")
            return None
        except Exception as e:
            print(f"Error processing table {table_name}: {e}")
            return None


def apply_special_cases(df, column_rename_map):
    DIVISION_CSV = "data/ncaa_divisions.csv"

    if "DIV_DIV" in column_rename_map:
        if os.path.exists(DIVISION_CSV):
            div_df = pd.read_csv(DIVISION_CSV)
            df = pd.merge(df, div_df, on="UNITID", how="left")
            df.rename(columns={"div": "DIV_DIV"}, inplace=True)
        else:
            print(f"Warning: Division CSV '{DIVISION_CSV}' not found.")

    for col in list(column_rename_map.keys()):
        if col.endswith("_DUP"):
            original_col = col[:-4]
            if original_col in df.columns:
                df[col] = df[original_col]
                print(f"Created '{col}' as a duplicate of '{original_col}'")
            else:
                print(
                    f"Warning: Cannot create '{col}' because '{original_col}' is missing."
                )

    phone_col = None
    for orig_col, renamed_col in column_rename_map.items():
        if renamed_col == "PHONE":
            phone_col = orig_col
            break

    if phone_col and phone_col in df.columns:

        def clean_phone(x):
            if pd.isnull(x):
                return None
            return x if len(str(x)) == 10 else None

        df[phone_col] = df[phone_col].apply(clean_phone)

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
                print(f"Converting '{col}' to pct.")
                df[original_col] = df[original_col] / 100.0
            else:
                print(f"'{col}' already has values less than or equal to 1.")

    pct_online_col = None
    for orig_col, renamed_col in column_rename_map.items():
        if renamed_col == "PCT_ONLINE_ONLY":
            pct_online_col = orig_col
            break

    if pct_online_col and pct_online_col in df.columns:
        df["ONLINE"] = df[pct_online_col].apply(
            lambda x: 1 if pd.notnull(x) and x > 0.5 else (2 if pd.notnull(x) else -1)
        )
        print("Created 'ONLINE' column based on '{}'.".format(pct_online_col))
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
            core.CITY,
            core.STATE,
            enrollment.TOTAL_POP AS POPULATION,
            enrollment.ONLINE
        FROM
            core, enrollment
        WHERE
            core.ID = enrollment.ID;
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


def get_source_table_for_col(column_name, schema):
    for table, columns in schema.items():
        if column_name in columns:
            return table
    return None


def main():
    ACCESS_DB_PATH = "data/IPEDS202324.accdb"
    SQL_OUTPUT_PATH = "data/universities.sqlite"
    DESCRIPTIONS_CSV_PATH = "data/descriptions.csv"

    if not os.path.exists(ACCESS_DB_PATH):
        print(f"Error: Access database not found at '{ACCESS_DB_PATH}'")
        return

    descriptions_df = get_access_table_data(
        ACCESS_DB_PATH, "DESCRIPTIONS", ["UNITID", "DESCRIPTION"]
    )
    if descriptions_df is not None:
        descriptions_df.to_csv(DESCRIPTIONS_CSV_PATH, index=False)
        print(f"Exported DESCRIPTIONS table to '{DESCRIPTIONS_CSV_PATH}'")

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

        filtered_df = apply_special_cases(filtered_df, rnmp)

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

    print("\nCreating 'search' view...")
    create_search_view(SQL_OUTPUT_PATH)
    print("View created successfully.")

    print("\nCreating 'descriptions' table...")
    create_descriptions_table(SQL_OUTPUT_PATH)
    print("Table 'descriptions' created successfully.")

    print("\nImporting descriptions from CSV...")
    if os.path.exists(DESCRIPTIONS_CSV_PATH):
        descriptions_df = pd.read_csv(DESCRIPTIONS_CSV_PATH, dtype={"UNITID": str})
        descriptions_df.to_sql("descriptions", engine, if_exists="replace", index=False)
        print(f"Descriptions imported from '{DESCRIPTIONS_CSV_PATH}'")
    else:
        print(f"Warning: Descriptions CSV '{DESCRIPTIONS_CSV_PATH}' not found.")

    if os.path.exists(DESCRIPTIONS_CSV_PATH):
        os.remove(DESCRIPTIONS_CSV_PATH)
        print(f"Deleted temporary file '{DESCRIPTIONS_CSV_PATH}'")


if __name__ == "__main__":
    main()
