import sqlite3

import pandas as pd

from rich import print

from score import scoring_components

conn = sqlite3.connect("data/sources/universities.sqlite")
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

df["SCORE"] = df.apply(lambda r: scoring_components(r, df), axis=1)
# df["SCORE"] = df["SCORE"].apply(lambda c: sum(c.values()))


cursor.execute(
    # "SELECT core.name, core.inst_control, core.endow_fte, enrollment.total_pop, enrollment.fte_pop FROM core INNER JOIN enrollment ON core.id = enrollment.id ORDER BY core.endow_fte * enrollment.fte_pop DESC LIMIT 50"
    "SELECT core.id, name, score, enrollment.online FROM core JOIN enrollment on core.id = enrollment.id ORDER BY core.score DESC LIMIT 100"
)

results = cursor.fetchall()

for num, row in enumerate(results):
    print(
        f"{'[red bold]ONLINE[/red bold]' if row[3] != 2 else ''}{num+1} {row[1]} - {round(row[2],2):,}pts ({row[0]})"
    )
    x = df[df["ID"] == row[0]]["SCORE"].values[0]
    # print(x)
    print(" ".join([f"{k}: {round(v,2)}" for k, v in x.items()]))
conn.close()
