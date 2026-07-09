import sqlite3

# Create or connect to memory database
connection = sqlite3.connect("database.db")

cursor = connection.cursor()

# Create memory table
cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT
)
""")

connection.commit()

connection.close()


def save_memory(key, value):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO memories (key, value)
        VALUES (?, ?)
        """,
        (key, value)
    )

    connection.commit()
    connection.close()


def get_memory(key):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT value FROM memories
        WHERE key = ?
        """,
        (key,)
    )

    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]
    else:
        return None