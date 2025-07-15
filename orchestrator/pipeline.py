# orchestrator/pipeline.py

from dagster import job, op
import subprocess

@op
def scrape_telegram_data():
    subprocess.run(["python", "loaders/scraper.py"], check=True)

@op
def load_raw_to_postgres():
    subprocess.run(["python", "loaders/load_raw_to_postgres.py"], check=True)

@op
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "medical_dbt"], check=True)

@op
def run_yolo_enrichment():
    subprocess.run(["python", "loaders/yolo_image_detection.py"], check=True)

@job
def healthcare_pipeline_job():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()

