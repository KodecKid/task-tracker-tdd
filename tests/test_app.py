# Import os to remove DB file between tests (ensures clean state)
import os
# Import unittest for TDD
import unittest
# Import DB_PATH to reset DB in setUp
from task_tracker.db import DB_PATH
# Import our app functions to test
from task_tracker import app

class TestTasks(unittest.TestCase):
    """
    Test suite for Task Tracker.
    - Demonstrates TDD: write tests first, then code to pass them.
    """

    def setUp(self):
        """
        Runs before each test.
        Removes the DB file so each test starts fresh.
        """
        if DB_PATH.exists():
            os.remove(DB_PATH)

    def test_add_task_inserts_row(self):
        """
        Test that adding a task actually stores it in the DB.
        - Red: fails before add_task is implemented.
        - Green: passes after implementation.
        """
        tid = app.add_task("Write TDD example")
        rows = app.list_tasks()
        self.assertTrue(any(r[0] == tid and r[1] == "Write TDD example" for r in rows))

    def test_mark_done_updates_status(self):
        """
        Test that mark_done changes a task's status to DONE.
        """
        tid = app.add_task("Learn TDD")
        self.assertTrue(app.mark_done(tid))
        done = [r for r in app.list_tasks("DONE") if r[0] == tid]
        self.assertEqual(len(done), 1)

    def test_search_tasks_finds_partial_title(self):
        """
        Test that search_tasks returns tasks matching a keyword.
        """
        app.add_task("Implement CRUD")
        app.add_task("Write README")
        hits = app.search_tasks("CRUD")
        self.assertTrue(any("CRUD" in r[1] for r in hits))

if __name__ == "__main__":
    unittest.main()
