from dagster import op
import subprocess

@op
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "medical_dbt"], check=True)
    return "DBT transformations complete"

