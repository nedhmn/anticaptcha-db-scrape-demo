# anticaptcha-db-scrape-demo

A Python web scraper that uses Anti-Captcha to bypass reCAPTCHA v3 and extract replay data from duelingbook.com.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Set environment variables in `.env`:
```
ANTICAPTCHA_API_KEY=your_api_key
SITE_KEY=target_website_site_key
```

## Usage

```bash
uv run python -m dbscrape.main
```

Scrapes replay data and saves JSON files to `data/replays/`.