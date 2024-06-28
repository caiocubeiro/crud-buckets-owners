import os
from dotenv import load_dotenv
import mysql.connector

db_config = {
    'host':  os.getenv("MARIA_HOST"),
    'user':   os.getenv("MARIA_USER"),
    'password':  os.getenv("MARIA_KEY"),
    'database': 'buckets_owners',
}

def connect_db():
    return mysql.connector.connect(**db_config)

def execute_query(query, params=None, fetchone=False, commit=False):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    if commit:
        conn.commit()
    if fetchone:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    conn.close()
    return result