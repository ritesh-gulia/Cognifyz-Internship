tasks = []


def add_task():
    title = input("Enter Task Name: ")
    tasks.append({"title": title, "status": "Pending"})
    print("✅ Task Added Successfully.")


def view_tasks():
    if not tasks:
        print("\nNo Tasks Available.\n")
        return

    print("\n========== TASK LIST ==========")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {task['status']}")


def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter Task Number to Update: ")) - 1

        if 0 <= index < len(tasks):
            new_title = input("Enter New Task Name: ")
            tasks[index]["title"] = new_title
            print("✅ Task Updated Successfully.")
        else:
            print("❌ Invalid Task Number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter Task Number to Delete: ")) - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("✅ Task Deleted Successfully.")
        else:
            print("❌ Invalid Task Number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def mark_completed():
    view_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter Task Number to Mark Completed: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Completed"
            print("✅ Task Marked as Completed.")
        else:
            print("❌ Invalid Task Number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def statistics():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["status"] == "Completed")
    pending = total - completed

    print("\n========== STATISTICS ==========")
    print(f"Total Tasks      : {total}")
    print(f"Completed Tasks  : {completed}")
    print(f"Pending Tasks    : {pending}")


while True:

    print("\n========== TASK MANAGER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Show Statistics")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        mark_completed()

    elif choice == "6":
        statistics()

    elif choice == "7":
        print("\nThank you for using Task Manager.")
        break

    else:
        print("Invalid Choice.")