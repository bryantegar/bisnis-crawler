import time
import logging
from crawler.core import fetch_articles
from crawler.utils import save_json

logging.basicConfig(level=logging.INFO)

INTERVAL = 60

def job():
    logging.info("Fetching latest articles...")
    data = fetch_articles()
    save_json(data, "latest.json")
    logging.info(f"Saved {len(data)} articles")


print("Running standard crawler...")

while True:
    job()
    time.sleep(INTERVAL)