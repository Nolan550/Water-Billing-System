from database.connections import get_connection
from datetime import date


def get_last_meter_reading(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT current_reading
        FROM meters
        WHERE customer_id = %s
        ORDER BY reading_date DESC
        LIMIT 1
    """, (customer_id,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return float(result[0])
    return 0


def add_meter_reading(customer_id, previous_reading, current_reading):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO meters (customer_id, previous_reading, current_reading, reading_date)
        VALUES (%s, %s, %s, %s)
    """, (customer_id, previous_reading, current_reading, date.today()))

    conn.commit()
    cur.close()
    conn.close()