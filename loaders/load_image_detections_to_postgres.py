import psycopg2

# Database connection config
conn = psycopg2.connect(
    host="localhost",
    database="telegram_medical",  
    user="your_username",
    password="your_password"
)
cur = conn.cursor()

# Create schema and table
cur.execute("""
    CREATE SCHEMA IF NOT EXISTS raw;

    CREATE TABLE IF NOT EXISTS raw.image_detections (
        message_id TEXT,
        detected_object_class TEXT,
        confidence_score FLOAT
    );
""")

conn.commit()
cur.close()
conn.close()
print("✅ Table 'raw.image_detections' created.")
