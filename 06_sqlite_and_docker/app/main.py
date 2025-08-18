import sqlite3

from datetime import datetime

# Connect to SQLite DB (new DB created if a DB does not exist)
conn = sqlite3.connect(database="data.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
""")

# Insert sample data
message = "Hello from Docker at " + datetime.now().isoformat()
cursor.execute(
    "INSERT INTO messages (content, timestamp) VALUES (?, ?)",
    (message, datetime.now().isoformat())
)

# Commit and close
conn.commit()
conn.close()

print("Data saved to SQLite!")
