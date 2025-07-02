import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import os
from data import data

access_db_path = "data/IPEDS202324.accdb"

sql_output_path = "data/universities.sql"
print(data["ADM2023"])
conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={os.getcwd()}/{access_db_path};"
)

conn = pyodbc.connect(conn_str)

hd = pd.read_sql(
    f"SELECT {", ".join(data["HD2023"])} FROM HD2023",
    conn,
)
ic = pd.read_sql("SELECT UNITID, CNTLAFFI FROM IC2023", conn)
ef = pd.read_sql("SELECT UNITID, STUFACR FROM EF2023D", conn)
drv = pd.read_sql("SELECT UNITID, DVADM01, DVADM04 FROM DRVADM2023", conn)

df = hd.merge(ic, on="UNITID").merge(ef, on="UNITID").merge(drv, on="UNITID")

df = df[  # TODO: Dont store these in the database, just use them for filtering
    (df["ICLEVEL"].isin([1, 2]))  # At least associate degree
    & (df["SECTOR"] != 0)  # Exlude Administrative units
    & (df["INSTSIZE"] > 0)  # Population reported
    & (df["CNTLAFFI"] > 0)  # Affiliation reported
    & (df["HDEGOFR1"] > 0)  # At least associate degree
    & (df["CYACTIVE"] == 1)  # Is active in current year
    & (df["POSTSEC"] == 1)  # Is primarily postsecondary
]

df_final = df.rename(
    columns={
        "UNITID": "id",
        "INSTNM": "name",
        "IALIAS": "alias",
        "INSTSIZE": "population",
        "DVADM01": "acceptance_rate",
        "DVADM04": "yield_rate",
        "STUFACR": "stu_fac",
        "HDEGOFR1": "highest_degree",
        "CNTLAFFI": "affiliation",
        "CITY": "city",
        "STABBR": "state",
        "LATITUDE": "coord_lat",
        "LONGITUD": "coord_long",
        "LOCALE": "locale",
    }
)[
    [
        "id",
        "name",
        "alias",
        "affiliation",
        "population",
        "acceptance_rate",
        "yield_rate",
        "stu_fac",
        "highest_degree",
        "city",
        "state",
        "coord_lat",
        "coord_long",
        "locale",
    ]
]

engine = create_engine(f"sqlite:///{sql_output_path}")
df_final.to_sql("universities", engine, if_exists="replace", index=False)

print(f"Exported {len(df_final)} universities to {sql_output_path}")
