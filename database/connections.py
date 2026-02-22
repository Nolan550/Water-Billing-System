import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="water_billing_db",
        user="postgres",
        password="database12",
        port="5433"
    )