# Import our DB helper functions
from .db import get_conn, init_db

def add_task(title: str) -> int:
    """
    Add a new task to the database.
    - Demonstrates 'Create' in CRUD.
    - Uses variables, data types, and input validation (conditionals).
    """
    if not title or not title.strip():
        raise ValueError("Title is required")  # Guard clause for invalid input
    init_db()  # Ensure DB and table exist
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO tasks(title) VALUES (?)",  # SQL parameterized query
            (title.strip(),)                        # Tuple with one element
        )
        return cur.lastrowid  # Return the new task's ID

def list_tasks(status: str | None = None) -> list[tuple]:
    """
    List all tasks, optionally filtered by status.
    - Demonstrates 'Read' in CRUD.
    - Uses conditionals and returns a list (array) of tuples.
    """
    init_db()
    with get_conn() as conn:
        if status:
            return list(conn.execute(
                "SELECT id, title, status, created_at FROM tasks WHERE status = ? ORDER BY created_at DESC",
                (status,)
            ))
        return list(conn.execute(
            "SELECT id, title, status, created_at FROM tasks ORDER BY created_at DESC"
        ))

def mark_done(task_id: int) -> bool:
    """
    Mark a task as DONE.
    - Demonstrates 'Update' in CRUD.
    - Returns True if a row was updated, False otherwise.
    """
    init_db()
    with get_conn() as conn:
        cur = conn.execute(
            "UPDATE tasks SET status = 'DONE' WHERE id = ?",
            (task_id,)
        )
        return cur.rowcount == 1  # Boolean check

def search_tasks(query: str) -> list[tuple]:
    """
    Search for tasks containing a given keyword in the title.
    - Demonstrates 'Read' with filtering (search).
    - Uses LIKE operator for partial matches.
    """
    init_db()
    q = f"%{query.strip()}%"  # Wildcards for partial match
    with get_conn() as conn:
        return list(conn.execute(
            "SELECT id, title, status, created_at FROM tasks WHERE title LIKE ? ORDER BY created_at DESC",
            (q,)
        ))