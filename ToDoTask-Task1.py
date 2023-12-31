#TO-DO LIST
#TASK 1
#A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists

tasks = []
while True:
    print("\n-------TO DO LIST-------")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit Program")

    select = input("Enter your selection (1/2/3): ")

    if select == '1':
        print("\n-------TASK ADD HERE-------")
        task = input("Add a task: ")
        tasks.append(task)
        print("Your Task added successfully!")
        print("---------------------------\n")
    if select == '2':
        if not tasks:
            
            print("Not any task available.")
        else:
            print("\n----------Available Tasks--------")
            for i, task in enumerate(tasks, start=1):
                print(f"Task {i}: {task}")
            print("---------------------------------\n") 
    if select == '3':
        if not tasks:
            print("No tasks available to delete.")
        else:
            print("\n----------Available Tasks--------")
            for i, task in enumerate(tasks, start=1):
                print(f"Task {i}: {task}")

            delete_index = int(input("Enter the task number to delete: "))
            if 1 <= delete_index <= len(tasks):
                deleted_task = tasks.pop(delete_index - 1)
                print(f"Task {delete_index}: {deleted_task} deleted successfully.")
            else:
                print("Invalid task number. Please try again.")
            print("---------------------------------\n")
    if select == '4':
        print("Program Exited...")
        break    