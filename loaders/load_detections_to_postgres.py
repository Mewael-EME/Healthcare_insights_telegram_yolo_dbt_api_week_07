import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to Postgres
conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)

cur = conn.cursor()

# Read detection results
df = pd.read_csv("data/yolo_detections.csv")

# Insert into raw table
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO raw.image_detections (message_id, detected_object_class, confidence_score)
        VALUES (%s, %s, %s)
    """, (row["image_id"], row["detected_object_class"], row["confidence_score"]))

conn.commit()
cur.close()
conn.close()

print("Detections loaded into raw.image_detections")
