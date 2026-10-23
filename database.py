import sqlite3

def get_connection():
    conn = sqlite3.connect("student.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name INTEGER NOT NULL ,age INTEGER,course TEXT NOT NULL)''')
    conn.commit()
    conn.close()
create_table()