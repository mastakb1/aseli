import mysql.connector
import pandas as pd
from dbConfig import read_config

def create_connection():
    config = read_config()
    print(f"Config read: {config}")  # Check if config is correctly populated
    try:
        conn = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def get_db_data(query):
    conn = create_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df