from database.connections import get_connection

def get_usage_by_sector():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT ct.type_name, SUM(b.consumption)
        FROM bills b
        JOIN customers c ON b.customer_id = c.customer_id
        JOIN customer_types ct ON c.type_id = ct.type_id
        GROUP BY ct.type_name
    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data