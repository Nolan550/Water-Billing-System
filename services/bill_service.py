from database.connections import get_connection

def create_bill(customer_id, month, year, consumption, amount_due):
    conn = get_connection()
    cur = conn.cursor()

    cur.exectue("""
                INSERT INTO bills(
                customer_id,
                billing_month,
                billing_year,
                consumption,
                amount_due,
                amount_paid,
                status)
                VALUES (%s, %s, %s, %s, %s,0, 'Unpaid')""",
                (customer_id, month, year, consumption, amount_due))
    
    conn.commit()
    cur.close()
    conn.close()


def get_bill_by_id(bill_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(""" SELECT bill_id, amount_due, amount_paid, status
                FROM bills
                WHERE bill_id = %s """, (bill_id,))
    
    bill = cur.fetchone()

    cur.close()
    conn.close()

    return bill