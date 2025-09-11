# Import sqlite3 to interact with SQLite databases (standard Python library)
import sqlite3
# Import Path to handle file paths in a cross-platform way
from pathlib import Path

# Define the path to the SQLite database file (stored in the same folder as this script)
DB_PATH = Path(__file__).parent / "task_tracker.db"

def get_conn():
    """
    Create and return a connection object to the SQLite database.
    This is part of 'Linking Data' in the activity — making a connection to the DB.
    """
    return sqlite3.connect(DB_PATH)

def init_db():
    """
    Initialize the database by creating the 'tasks' table if it doesn't exist.
    Demonstrates executing a CREATE statement (part of CRUD).
    """
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each task
                title TEXT NOT NULL,                   -- Task description
                status TEXT NOT NULL DEFAULT 'OPEN',   -- Task status (OPEN/DONE)
                created_at TEXT NOT NULL DEFAULT (datetime('now')) -- Timestamp
            )
        """)
