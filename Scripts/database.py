import sqlite3

DB_PATH = "Saves/players.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row #Чтобы обращаться по имени колонки
    return conn

