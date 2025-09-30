import requests
import csv

FOUNDING_CSV = "data/out/founding.csv"

url = "https://query.wikidata.org/sparql"

query = """
SELECT DISTINCT (YEAR(?foundingDate) AS ?foundyr) (?ipedsID AS ?UNITID) WHERE {
    ?school wdt:P31/wdt:P279* wd:Q3918;
                    wdt:P17 wd:Q30.
    OPTIONAL { ?school wdt:P571 ?foundingDate. }
    OPTIONAL { ?school wdt:P1771 ?ipedsID. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY ?schoolLabel
"""

headers = {
    "User-Agent": "UniSearch/1.0 (https://college.underscore.wtf/; lior.pendler@gmail.com)"
}

response = requests.get(url, params={"query": query, "format": "json"}, headers=headers)
response.raise_for_status()
data = response.json()

rows = data["results"]["bindings"]

seen_ipeds = set()
filtered_rows = []

for r in rows:
    unitid = r.get("UNITID", {}).get("value", "")
    foundyr = r.get("foundyr", {}).get("value", "")
    if unitid and foundyr and unitid not in seen_ipeds:
        filtered_rows.append([unitid, foundyr])
        seen_ipeds.add(unitid)

with open(FOUNDING_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["UNITID", "foundyr"])
    writer.writerows(filtered_rows)

print(f"Saved to {FOUNDING_CSV}")
