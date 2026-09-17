# Week 2 Debugging Log

## Scope

This debugging exercise uses `original_buggy_task_tracker.py`, a deliberately faulty command-line task tracker. The goal was to reproduce each issue, identify its cause, apply a focused correction, and verify that the corrected program remains easy to read and maintain.

## Debugging Approach

1. Read each function and trace how data moves from user input to the task list.
2. Reproduce failures with small manual test cases.
3. Use breakpoints or `pdb` around the failing function when needed. For example: `python -m pdb original_buggy_task_tracker.py`.
4. Fix one issue at a time and run the unit tests after each meaningful change.
5. Refactor duplicated or unclear logic only when it preserves the intended behavior.

## Bug Report

| ID | Reproduction and observed behavior | Root cause | Resolution |
|---|---|---|---|
| B1 | Choose View Tasks when at least one task exists. The script eventually raises `IndexError: list index out of range`. | `range(len(tasks) + 1)` includes one index beyond the final valid list index. | Replaced manual indexing with `enumerate(tasks, start=1)` in `view_tasks`. |
| B2 | Choose Complete Task and enter `1`. The script raises `TypeError: list indices must be integers or slices, not str`. | `input()` always returns text, but the value was used as a list index. | Added numeric conversion in `get_task_number` and handled `ValueError`. |
| B3 | Enter a task number such as `99`. The script raises an unhandled `IndexError`. | There was no check that the task number was within the list range. | Added a one-based range check and raised a clear `ValueError`. |
| B4 | Add a blank task title. The script accepts it and creates an unusable task. | `add_task` had no validation. | Stripped whitespace and rejected empty titles with a descriptive error. |
| B5 | Choose Exit. The program prints Goodbye but returns to the menu. | The exit branch did not stop the loop. | Added `break` after the exit message. |
| B6 | Task state was represented by changing the task title text. | A title and a completion state are separate pieces of data. | Introduced a `Task` dataclass with `title` and `completed` fields. |

## Before and After Example

Original unsafe loop:

```python
for index in range(len(tasks) + 1):
    print(f"{index + 1}. {tasks[index]}")
```

Corrected safe implementation:

```python
return [
    f"{index}. {task.title} [{'Completed' if task.completed else 'Pending'}]"
    for index, task in enumerate(tasks, start=1)
]
```

## Validation

Automated tests cover valid task creation, empty-title validation, safe empty-list viewing, task completion, and invalid task numbers. Run them from this folder:

```bash
python -m unittest test_corrected_task_tracker.py
```

Manual checks should include invalid menu choices, non-numeric task numbers, a missing task number, and exiting the application. The corrected script handles these cases without crashing.

## Improvements Made

The corrected version separates task data from command-line interaction, uses type hints and docstrings, centralizes validation, and returns formatted data from `view_tasks` rather than mixing display formatting with list manipulation. These changes improve readability and make the program easier to test and extend.
