from database.connections import get_connection


def get_customer_type_by_name(type_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT type_id, rate_per_unit
        FROM customer_types
        WHERE type_name = %s
    """, (type_name,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return {
            "type_id": result[0],
            "rate_per_unit": float(result[1])
        }
    return None


def add_customer(first, last, address, phone, type_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO customers (first_name, last_name, address, phone, type_id)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING customer_id
    """, (first, last, address, phone, type_id))

    customer_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return customer_id


def get_customer_bills(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT bill_id, billing_month, billing_year, amount_due, amount_paid, status
        FROM bills
        WHERE customer_id = %s
        ORDER BY billing_year DESC
    """, (customer_id,))

    bills = cur.fetchall()

    cur.close()
    conn.close()

    return bills