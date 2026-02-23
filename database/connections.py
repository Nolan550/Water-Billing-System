import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="water_billing_db2",
        user="postgres",
        password="nolan1234",
        port="5432"
    )