"""Automated tests for corrected_task_tracker.py."""

import unittest

from corrected_task_tracker import add_task, complete_task, view_tasks


class TaskTrackerTests(unittest.TestCase):
    def setUp(self):
        self.tasks = []

    def test_add_task_creates_pending_task(self):
        task = add_task(self.tasks, "Review Python code")
        self.assertEqual(task.title, "Review Python code")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.tasks), 1)

    def test_empty_task_title_is_rejected(self):
        with self.assertRaises(ValueError):
            add_task(self.tasks, "   ")

    def test_viewing_an_empty_list_is_safe(self):
        self.assertEqual(view_tasks(self.tasks), ["No tasks found."])

    def test_complete_task_changes_status(self):
        add_task(self.tasks, "Write tests")
        task = complete_task(self.tasks, 1)
        self.assertTrue(task.completed)
        self.assertIn("Completed", view_tasks(self.tasks)[0])

    def test_invalid_task_number_is_rejected(self):
        add_task(self.tasks, "Write tests")
        with self.assertRaises(ValueError):
            complete_task(self.tasks, 2)


if __name__ == "__main__":
    unittest.main()
