from dagster import op
import subprocess

@op
def run_yolo_enrichment():
    subprocess.run(["python", "yolo/image_detector.py"], check=True)
    return "YOLO enrichment complete"

