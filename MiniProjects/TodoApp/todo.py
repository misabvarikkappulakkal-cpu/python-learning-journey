tasks = []

while True:
    print("\n==== TODO APP ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print("-", task)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        task = input("Enter task to remove: ")

        if task in tasks:
            tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found.")

    elif choice == "4":
        print("Exiting Todo App...")
        break

    else:
        print("Invalid choice. Try again.")
