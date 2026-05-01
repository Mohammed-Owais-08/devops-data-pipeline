import sqlite3

def load(data):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        city TEXT,
        temp REAL,
        weather TEXT
    )
    """)

    cursor.execute("INSERT INTO weather VALUES (?, ?, ?)",
                   (data["city"], data["temp"], data["weather"]))

    conn.commit()
    conn.close()