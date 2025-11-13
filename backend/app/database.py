
import sqlite3
import os

DB_PATH = "listings.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            price REAL,
            size_m2 REAL,
            location TEXT,
            floor INTEGER,
            heating TEXT,
            orientation TEXT,
            parking INTEGER,
            investment_score REAL,
            scam_score REAL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_conn():
    return sqlite3.connect(DB_PATH)
