import bcrypt
from database.connections import get_connection


def register_user(username, password, role):
    conn = get_connection()
    cur = conn.cursor()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cur.execute("""
        INSERT INTO users (username, password_hash, role)
        VALUES (%s, %s, %s)
    """, (username, hashed.decode(), role))

    conn.commit()
    cur.close()
    conn.close()


def login_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT user_id, password_hash, role
        FROM users
        WHERE username = %s
    """, (username,))

    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        stored_hash = user[1].encode()
        if bcrypt.checkpw(password.encode(), stored_hash):
            return {
                "user_id": user[0],
                "role": user[2]
            }

    return None