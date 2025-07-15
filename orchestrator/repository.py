from dagster import repository
from jobs import full_pipeline
from schedules import daily_pipeline

@repository
def orchestrator_repo():
    return [full_pipeline, daily_pipeline]
