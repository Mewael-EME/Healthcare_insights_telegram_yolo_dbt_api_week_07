# api/crud.py
from .database import get_db_connection

def get_top_products(limit: int = 10):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT LOWER(unnested_word) AS product, COUNT(*) as count
        FROM (
            SELECT unnest(string_to_array(message, ' ')) as unnested_word
            FROM fct_messages
        ) AS words
        GROUP BY product
        ORDER BY count DESC
        LIMIT %s
    """
    cursor.execute(query, (limit,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_channel_activity(channel_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT sent_at::date as date, COUNT(*) as message_count
        FROM fct_messages
        WHERE LOWER(channel) = LOWER(%s)
        GROUP BY date
        ORDER BY date ASC
    """
    cursor.execute(query, (channel_name,))
    results = cursor.fetchall()
    conn.close()
    return results

def search_messages(query_term: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT message, channel, sent_at
        FROM fct_messages
        WHERE LOWER(message) LIKE %s
        ORDER BY sent_at DESC
        LIMIT 50
    """
    cursor.execute(query, (f"%{query_term.lower()}%",))
    results = cursor.fetchall()
    conn.close()
    return results

