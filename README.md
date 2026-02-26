# Bisnis.com Article Crawler

Python crawler untuk mengambil artikel dari situs bisnis.com.

## Features
- Scrape artikel dari kategori bisnis.com
- Dua mode:
  - Backtrack Mode → ambil artikel berdasarkan range tanggal
  - Standard Mode → ambil artikel terbaru secara berkala
- Error handling & retry mechanism
- Logging system
- JSON output clean format

---

## Architecture

Project menggunakan modular architecture:

crawler/
 ├ core.py      → crawling engine
 ├ parser.py    → parsing logic
 └ utils.py     → helper functions

Entry points:
- backtrack.py
- standard.py

Crawler menggunakan category pages instead of homepage karena homepage menggunakan dynamic rendering.

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Usage

### Backtrack Mode

python backtrack.py 2026-02-01 2026-02-26

Output:
backtrack.json


### Standard Mode

python standard.py

Output:
latest.json (update berkala)

---

## Output Format

[
  {
    "link": "...",
    "judul": "...",
    "isi": "...",
    "tanggal": "ISO 8601"
  }
]

---

## Engineering Notes

Crawler dirancang dengan pendekatan production-style:

- retry request handling
- structured logging
- robust parsing
- defensive scraping strategy

---

## Author
Bryan Tegar