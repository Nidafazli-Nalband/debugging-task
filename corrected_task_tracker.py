"""Corrected command line task tracker for the Week 2 debugging exercise."""

from dataclasses import dataclass


@dataclass
class Task:
    """A single task with a title and completion state."""

    title: str
    completed: bool = False


def add_task(tasks: list[Task], title: str) -> Task:
    """Validate and add a task to the supplied list."""
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("Task title cannot be empty.")

    task = Task(title=cleaned_title)
    tasks.append(task)
    return task


def view_tasks(tasks: list[Task]) -> list[str]:
    """Return formatted task lines without printing outside the list bounds."""
    if not tasks:
        return ["No tasks found."]

    return [
        f"{index}. {task.title} [{'Completed' if task.completed else 'Pending'}]"
        for index, task in enumerate(tasks, start=1)
    ]


def complete_task(tasks: list[Task], task_number: int) -> Task:
    """Mark a one-based task number as completed after validating it."""
    if not 1 <= task_number <= len(tasks):
        raise ValueError("Task number does not exist.")

    task = tasks[task_number - 1]
    task.completed = True
    return task


def get_task_number() -> int | None:
    """Read a numeric task number and avoid crashing on text input."""
    try:
        return int(input("Task number: "))
    except ValueError:
        print("Please enter a numeric task number.")
        return None


def main() -> None:
    """Run the interactive task tracker menu."""
    tasks: list[Task] = []

    while True:
        print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                task = add_task(tasks, input("Task title: "))
                print(f"Task added: {task.title}")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            print("\n".join(view_tasks(tasks)))
        elif choice == "3":
            task_number = get_task_number()
            if task_number is not None:
                try:
                    task = complete_task(tasks, task_number)
                    print(f"Task completed: {task.title}")
                except ValueError as error:
                    print(f"Error: {error}")
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid option. Choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
