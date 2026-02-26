import requests
from bs4 import BeautifulSoup
from dateutil import parser
import logging

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def parse_article(url):
    res = requests.get(url, headers=HEADERS, timeout=10)

    if res.status_code != 200:
        raise Exception("Request failed")

    soup = BeautifulSoup(res.text, "html.parser")

    title_meta = soup.find("meta", property="og:title")
    if not title_meta:
        raise Exception("Title not found")
    title = title_meta["content"]

    date_meta = soup.find("meta", property="article:published_time")
    if not date_meta:
        raise Exception("Date not found")

    date_iso = parser.parse(date_meta["content"]).isoformat()

    paragraphs = soup.find_all("p")
    content = "\n".join(
        p.get_text(strip=True)
        for p in paragraphs
        if p.get_text(strip=True)
    )

    return {
        "link": url,
        "judul": title,
        "isi": content,
        "tanggal": date_iso
    }