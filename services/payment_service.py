from database.connections import get_connection
from decimal import Decimal

def process_payment(bill_id, payment_amount):
    conn = get_connection()
    cur = conn.cursor()

    try:
        payment_amount = Decimal(payment_amount)

        cur.execute("""
                    SELECT amount_due, amount_paid
                    FROM bills
                    WHERE bill_id = %s
                    FOR UPDATE
                    """, (bill_id,))
        
        bill = cur.fetchone()

        if not bill:
            raise Exception("Bill not found")
        
        amount_due, amount_paid = bill

        new_amount_paid = amount_paid + payment_amount


        if new_amount_paid == 0:
            status = "Unpaid"
        elif new_amount_paid < amount_due:
            status = "Partially Paid"
        else:
            status = "Paid"

        cur.execute("""
                    UPDATE bills
                    SET amount_paid = %s,
                    status = %s
                    WHERE bill_id = %s
                    """, (new_amount_paid, status, bill_id))
        conn.commit()

        return {
            "new_amount_paid": new_amount_paid,
            "status": status
        }
    except Exception as e:
        conn.rollback()
        print("Payment error:", e)
        return None
    
    finally:
        cur.close()
        conn.close()
        




def get_payment_history(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.payment_id,
               p.amount_paid,
               p.payment_date,
               p.bill_id
        FROM payments p
        JOIN bills b ON p.bill_id = b.bill_id
        WHERE b.customer_id = %s
        ORDER BY p.payment_date DESC
    """, (customer_id,))

    payments = cur.fetchall()

    cur.close()
    conn.close()

    return payments