def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        
        print("\nOptions: [1] Add Task [2] Remove Task [3] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
        elif choice == '2':
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
            else:
                print("Invalid task number.")
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")

todo_list()
