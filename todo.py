tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks):
        status = "✔" if task["done"] else "❌"
        print(f"{idx + 1}. [{status}] {task['task']}")

def mark_done(index):
    try:
        tasks[index - 1]["done"] = True
        print("Task marked as done.")
    except IndexError:
        print("Invalid task number.")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Deleted task: {removed['task']}")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as done: "))
            mark_done(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()
