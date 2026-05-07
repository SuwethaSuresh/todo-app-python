import json

tasks = []

# Load tasks
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []

# Save tasks
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task():
    title = input("Enter task title: ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!\n")

# View tasks
def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n===== Tasks =====")
    for i, task in enumerate(tasks, 1):
        status = "✔ Completed" if task["completed"] else "✘ Pending"
        print(f"{i}. {task['title']} | {task['priority']} | {task['due_date']} | {status}")
    print()

# Mark complete
def mark_complete():
    view_tasks()
    try:
        index = int(input("Enter task number: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks()
            print("Task marked as completed!\n")
        else:
            print("Invalid index!\n")
    except:
        print("Invalid input!\n")

# Delete task
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks()
            print("Task deleted!\n")
        else:
            print("Invalid index!\n")
    except:
        print("Invalid input!\n")

# Menu
def menu():
    load_tasks()

    while True:
        print("===== To-Do Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice!\n")

menu()
