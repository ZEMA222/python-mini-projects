choice = None 
TaskList = []

while choice != 4:
    print("Menu:")
    print("1- Add Task")
    print("2- Del Task")
    print("3- View Tasks")
    print("4- Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue 
    
    match choice:
        case 1:
            task = input("What are u planning to do: ")
            TaskList.append(task)
            print(f"✔ Task '{task}' added successfully!")
            
        case 2:
            if len(TaskList) == 0:
                print("List is Empty!")
            else:
                task_to_del = input("Enter Task's name to delete: ")
                if task_to_del in TaskList:
                    TaskList.remove(task_to_del)
                    print(f"❌ Task '{task_to_del}' deleted successfully!")
                else: 
                    print("There is no such a task!")
                    
        case 3:
            if len(TaskList) == 0:
                print("Your task list is empty!")
            else:
                print("\nHere is your task List:")
                for index, t in enumerate(TaskList, 1):
                    print(f"{index}- {t}")
                    
        case 4:
            print("Good Luck Hero! \nHave a nice day!")
            
        case _:
            print("Error! \ninvalid input")