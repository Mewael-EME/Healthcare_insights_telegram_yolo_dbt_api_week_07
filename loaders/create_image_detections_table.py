import psycopg2

# Step 1: Connect to your database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="telegram_medical",
    user="postgres",
    password="2328"
)
cur = conn.cursor()

# Step 2: Create schema and table
cur.execute("""
    CREATE SCHEMA IF NOT EXISTS raw;

    CREATE TABLE IF NOT EXISTS raw.image_detections (
        message_id TEXT,
        detected_object_class TEXT,
        confidence_score FLOAT
    );
""")

# Step 3: Clean up
conn.commit()
cur.close()
conn.close()
print("✅ Table raw.image_detections has been created.")
