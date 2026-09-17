"""Original deliberately buggy script used for the Week 2 debugging exercise."""


def add_task(tasks, title):
    # Bug: empty titles are accepted and task IDs are not stored.
    tasks.append(title)
    print("Task added")


def view_tasks(tasks):
    # Bug: the final loop iteration accesses an index outside the list.
    for index in range(len(tasks) + 1):
        print(f"{index + 1}. {tasks[index]}")


def complete_task(tasks, task_id):
    # Bug: task_id is received as text but is used as a list index.
    tasks[task_id] = tasks[task_id] + " (completed)"


def main():
    tasks = []

    while True:
        print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks, input("Task title: "))
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks, input("Task number: "))
        elif choice == "4":
            print("Goodbye")
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
