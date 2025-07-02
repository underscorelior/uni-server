import os
import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from data import schema_2, data


def get_source_table_for_col(column_name, schema):
    for table, columns in schema.items():
        if column_name in columns:
            return table
    return None


def main():
    access_db_path = "data/IPEDS202324.accdb"
    sql_output_path = "data/universities.sqlite"
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={os.path.abspath(access_db_path)};"
    )

    if not os.path.exists(access_db_path):
        print(f"Error: Access database not found at '{access_db_path}'")
        return

    try:
        conn = pyodbc.connect(conn_str)
        print("Successfully connected to Access database.")
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error connecting to Access DB: {sqlstate}")
        return

    os.makedirs(os.path.dirname(sql_output_path), exist_ok=True)
    if os.path.exists(sql_output_path):
        os.remove(sql_output_path)
    engine = create_engine(f"sqlite:///{sql_output_path}")

    filter_columns = [
        "ICLEVEL",
        "SECTOR",
        "DEATHYR",
        "CYACTIVE",
        "DEGGRANT",
        "INSTSIZE",
        "POSTSEC",
    ]

    for new_table_name, column_rename_map in schema_2.items():
        source_cols_for_this_table = list(column_rename_map.keys())
        source_tables_to_query = {}
        for col in source_cols_for_this_table:
            source_table = get_source_table_for_col(col, data)
            if source_table:
                if source_table not in source_tables_to_query:
                    source_tables_to_query[source_table] = set()
                source_tables_to_query[source_table].add(col)
        if "HD2023" not in source_tables_to_query:
            source_tables_to_query["HD2023"] = set()
        source_tables_to_query["HD2023"].update(filter_columns)

        if not source_tables_to_query:
            print(f"Skipping table '{new_table_name}' as no source columns were found.")
            continue

        dataframes = {}
        for table_name, columns in source_tables_to_query.items():
            columns.add("UNITID")
            col_str = ", ".join(f"[{c}]" for c in columns)
            query = f"SELECT {col_str} FROM {table_name}"
            print(f"  Querying source table '{table_name}'...")
            try:
                dataframes[table_name] = pd.read_sql(query, conn)
            except pd.io.sql.DatabaseError as e:
                print(f"  ERROR reading table '{table_name}': {e}")
                continue

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

        final_cols_original_names = [
            col for col in column_rename_map.keys() if col in filtered_df.columns
        ]
        if "UNITID" not in final_cols_original_names:
            final_cols_original_names.insert(0, "UNITID")

        new_table_df = filtered_df[final_cols_original_names].copy()
        new_table_df.rename(columns=column_rename_map, inplace=True)

        new_table_df.to_sql(new_table_name, engine, if_exists="replace", index=False)
        print(f"  Exported '{new_table_name}' - {len(new_table_df.columns)} columns.")

    conn.close()
    print(f"\nSuccess! All tables exported to '{sql_output_path}'")


if __name__ == "__main__":
    main()
