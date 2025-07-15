from dagster import op
import subprocess

@op
def scrape_telegram_data():
    subprocess.run(["python", "scraper/scraper.py"], check=True)
    return "Scraping complete"