import sys
from datetime import datetime
from crawler.core import fetch_articles
from crawler.utils import save_json

print("Program started...")

if len(sys.argv) < 3:
    print("Usage: python backtrack.py <start_date> <end_date>")
    sys.exit()

start = datetime.fromisoformat(sys.argv[1])
end = datetime.fromisoformat(sys.argv[2])

print("Fetching articles...")
articles = fetch_articles(max_pages=1)

filtered = []

for a in articles:
    try:
        article_date = datetime.fromisoformat(a["tanggal"]).date()
        if start.date() <= article_date <= end.date():
            filtered.append(a)

    except Exception as e:
    	print("Skip error:", e)

save_json(filtered, "backtrack.json")

print("Done:", len(filtered), "artikel disimpan")