from dagster import schedule
from jobs import full_pipeline

@schedule(cron_schedule="0 2 * * *", job=full_pipeline, execution_timezone="Africa/Addis_Ababa")
def daily_pipeline():
    return {}
