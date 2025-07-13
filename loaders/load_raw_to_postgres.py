import os
import json
import psycopg2
from glob import glob
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL connection settings (use env vars)
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_USER = os.getenv("PG_USER", "postgres")
PG_PASS = os.getenv("PG_PASS", "postgres")
PG_DB   = os.getenv("PG_DB", "telegram_db")

def load_json_to_postgres():
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE SCHEMA IF NOT EXISTS raw;
        CREATE TABLE IF NOT EXISTS raw.telegram_messages (
            id SERIAL PRIMARY KEY,
            data JSONB
        );
    """)
    conn.commit()

    json_files = glob("data/raw/telegram_messages/**/*.json", recursive=True)

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            messages = json.load(f)
            for message in messages:
                cur.execute("INSERT INTO raw.telegram_messages (data) VALUES (%s)", [json.dumps(message)])

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Inserted {len(messages)} messages from {file_path}")

if __name__ == "__main__":
    load_json_to_postgres()
