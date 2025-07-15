from dagster import job
from ops.scrape import scrape_telegram_data
from ops.load import load_raw
from ops.transform import run_dbt
from ops.enrich import run_yolo

@job
def full_pipeline():
    msgs = scrape_telegram_data()
    loaded = load_raw(msgs)
    transformed = run_dbt(loaded)
    run_yolo(transformed)
