# Simple To-Do List Application (Console-based)

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task
def add_task(tasks):
    task = input("Enter task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
