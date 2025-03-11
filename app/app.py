from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="postgres",
            port="5432"
        )
        return "Connected to PostgreSQL!"
    except:
        return "Database connection failed!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
