# orchestrator/__init__.py

from dagster import Definitions
from .pipeline import healthcare_pipeline_job

defs = Definitions(
    jobs=[healthcare_pipeline_job]
)
