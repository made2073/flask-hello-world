import os
import psycopg2

from flask import Flask
app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route('/')
def index():
    return 'Hello World from Matthew DeBusk in 3308'

@app.route("/db_test")
def ddb_test():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database successfully connected."
    except Exception as e:
        return f"Database failed connection: {e}"
    finally:
        if conn is not None:
            conn.close()