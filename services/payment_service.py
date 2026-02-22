from database.connections import get_connection


def process_payment(bill_id, payment_amount):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                INSERT INTO payments(bill_id, amount_paid)
                VALUES (%s, %s)""",
                (bill_id, payment_amount))
    
    cur.execute("""
            UPDATE bills
            SET status = 
                CASE
                    WHEN amount_paid >= amount_due THEN 'Paid'
                    WHEN amount_paid > 0 THEN 'Partially paid'
                    ELSE 'Unpaid'
                END
            WHERE bill-id = %s
            """, (bill_id,))
    
    conn.commit()
    cur.close()
    conn.close()