tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {task['task']} {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task["task"])

            num = int(input("Enter task number to remove: "))
            tasks.pop(num - 1)
            print("Task removed!")

    elif choice == "4":
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task["task"])

            num = int(input("Enter task number to mark done: "))
            tasks[num - 1]["done"] = True
            print("Task marked as done!")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

    else:
