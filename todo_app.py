from datetime import datetime, timedelta

ListofTasks= []


def addTask():
    
    dataHolder= {
    "Task": None,
    "Time": None,
    "Due": None 
    }
    
    Name= input("Enter task name: ")
    TaskTime= int(input("Enter task time (in minutes): "))
    
    current_time_24hr = datetime.now().strftime("%H:%M")
    current_time_24hr_obj= datetime.strptime(current_time_24hr, "%H:%M")
    
    DueTime= current_time_24hr_obj + timedelta(minutes=TaskTime)
    DueTime= DueTime.strftime("%H:%M")
    
    dataHolder["Task"]= Name
    dataHolder["Time"]= TaskTime
    dataHolder["Due"]= DueTime
    
    ListofTasks.append(dataHolder)

def removeTask():
    if not ListofTasks: 
        print("you have no tasks in your list")
    else:
        viewTasks()
        taskIndex= int(input("Enter the number of task to be removed: ")) - 1
        removedTask= ListofTasks.pop(taskIndex)
        print(f"{removedTask['Task']} task is removed from the list")

def viewTasks():
    for i in range(len(ListofTasks)):
        current_task= ListofTasks[i]
        print(f"\n Task {i+1}: \n\tName: {current_task['Task']} \n\tDuration: {current_task['Time']} \n\tDue Time: {current_task['Due']} \n")
        

while True: 
    print("Select the operation you to perform:\n 1. Add Task \n 2. Remove task \n 3. View tasks \n 4. Exit")
    choice= int(input())
    if choice == 1:
        addTask()
    elif choice == 2:
        removeTask()
    elif choice == 3:
        viewTasks()
    elif choice==4:
        break
    else:
        print("Enter the correct operation!!!")

