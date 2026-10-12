import sqlite3

DB_PATH = "Saves/players.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row #Чтобы обращаться по имени колонки
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute('''
        create table if not exists players(
            id integer primary key autoincrement,
            name text not null unique,
            level integer not null default 1,
            points integer not null default 0
        )
        ''')