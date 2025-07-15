from dagster import op
import subprocess

@op
def load_raw_to_postgres(_):
    subprocess.run(["python", "loaders/load_raw_to_postgres.py"], check=True)
    return "Load complete"

