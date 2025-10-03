tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully!")
    
    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✔ Done" if t["done"] else "Pending"
                print(f"{i}. {t['task']} [{status}]")
    
    elif choice == '3':
        task_no = int(input("Enter task number to mark as done: "))
        if 0 < task_no <= len(tasks):
            tasks[task_no-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    
    elif choice == '4':
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no-1)
            print(f"Task '{removed['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    
    elif choice == '5':
        print("Exiting To-Do List... Goodbye!")
        break
    
    else:
        print("Invalid choice. Try again.")