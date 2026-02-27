import requests
from bs4 import BeautifulSoup
import logging
import time

logging.basicConfig(level=logging.INFO)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

SOURCES = [
    "https://ekonomi.bisnis.com",
    "https://market.bisnis.com",
    "https://finansial.bisnis.com"
]


def request_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            return requests.get(url, headers=HEADERS, timeout=10)
        except Exception as e:
            logging.warning(f"Retry {attempt+1} failed: {e}")
            time.sleep(1)
    raise Exception("Request failed after retries")


def get_article_links():
    links = []

    for source in SOURCES:
        res = request_with_retry(source)
        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a", href=True):
            href = a["href"]

            if "/read/" in href:
                if href.startswith("http"):
                    links.append(href)
                else:
                    links.append("https://" + source.split("//")[1] + href)

    unique_links = list(set(links))
    logging.info(f"Fetched {len(unique_links)} links")
    return unique_links


def fetch_articles(max_pages=1):
    from .parser import parse_article

    links = get_article_links()
    articles = []
    skipped = 0

    for link in links:
        try:
            data = parse_article(link)
            articles.append(data)
        except Exception:
            skipped += 1

    print(f"Fetched {len(links)} links")
    print(f"Skipped {skipped} articles due to parsing issues")
    print(f"Saved {len(articles)} articles")

    return articles

    for link in links:
        try:
            data = parse_article(link)
            articles.append(data)
        except Exception as e:
            skipped += 1

        print(f"Fetched {len(links)} links")
        print(f"Skipped {skipped} articles due to parsing issues")
        print(f"Saved {len(articles)} articles")

        return articles