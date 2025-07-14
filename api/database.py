# api/database.py
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import psycopg2

load_dotenv()  # Load .env variables into environment

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        database=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASS"),
        cursor_factory=RealDictCursor
    )

