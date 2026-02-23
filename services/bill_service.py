from database.connections import get_connection
from decimal import Decimal

def create_bill(customer_id, month, year):
    conn = get_connection()
    cur = conn.cursor()


    try:
        cur.execute("""
                    SELECT previous_reading, current_reading
                    FROM meters
                    WHERE customer_id = %s
                    ORDER BY reading_date DESC
                    LIMIT 1
            """, (customer_id,))
        
        meter = cur.fetchone()

        if not meter:
            raise Exception("No meter reading found for customer")
        

        previous_reading, current_reading = meter
        consumption = current_reading - previous_reading


        if consumption < 0:
            raise Exception("Invalid meter readings")
        
        cur.execute("""
                SELECT ct.rate_per_unit
                FROM customers c
                JOIN customer_types ct ON c.type_id = ct.type_id
                WHERE c.customer_id = %s
        """, (customer_id,))

        rate = cur.fetchone()

        if not rate:
            raise Exception("Customer type not found")
        
        rate_per_unit = (rate[0])
        cosnumption = Decimal(consumption)
        amount_due = consumption * rate_per_unit
        
        cur.execute("""
                INSERT INTO bills(
                customer_id,
                billing_month,
                billing_year,
                consumption,
                amount_due,
                amount_paid,
                status)
                VALUES (%s, %s, %s, %s, %s,0, 'Unpaid')
                RETURNING bill_id""",
                (customer_id, month, year, consumption, amount_due))
    
        bill_id = cur.fetchone()[0]
    
        conn.commit()
        return bill_id


    except Exception as e:
        conn.rollback()
        print("Error creating bill:", e)
        return None
    finally:

        cur.close()
        conn.close()


def get_customer_bills(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
                    SELECT bill_id,
                    billing_month,
                    billing_year,
                    consumption,
                    amount_due,
                    amount_paid,
                    status
                    FROM bills
                    WHERE customer = %s
                    ORDER BY billing-year DESC, billing_month DESC
                    """, (customer_id,))
        
        rows = cur.fetchall()
        bills= []

        for row in rows:
            bills.append({
                "bill_id": row[0],
                "month": row[1],
                "year": row[2],
                "consumption": row[3],
                "amount_due": row[4],
                "amount-paid": row[5],
                "status": row[6]
            })

        return bills
    except Exception as e:
        print("Error fetching bills:", e)
        return []
    
    finally:
        cur.close()
        conn.close()


