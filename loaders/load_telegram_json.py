import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="telegram_medical",
    user="postgres",
    password="yourpassword"
)
cur = conn.cursor()

with open("data/messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

for msg in messages:
    cur.execute("""
        INSERT INTO raw_telegram_messages (message_id, sender, text, date, channel, has_media)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        msg.get("id"),
        msg.get("sender"),
        msg.get("text"),
        msg.get("date"),
        msg.get("channel"),
        bool(msg.get("media"))
    ))

conn.commit()
cur.close()
conn.close()
