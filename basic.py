
print("""--- TO-DO LIST --- \n
1. Add Task\n
2. View Tasks\n
3. Mark Task as Done\n
4. Delete Task\n
5. Exit\n""")

tasksDict ={}


while True:
   
    try:
        choice = int(input("Enter your choice: "))
        if choice==1:
            newTask = str(input("Enter new task: "))
            tasksDict[len(tasksDict)+1] = {newTask:'nd'}
            print("Task added!")
            # print(tasksDict)
        elif choice ==2:
            listOfTasks= list(tasksDict.values())
            
            # print(listOfTasks)
            for item in listOfTasks:
                # print(list(item.keys())[0])
                # print(list(item.values())[0])
                status = list(item.values())[0]
                # print(f'status: {status}')
                print(f'[✔] {list(item.keys())[0]}' if status=='done' else f'[ ] {list(item.keys())[0]}')             
        elif choice==3:
            doneTaskNumber = int(input('Which Task to mark as done? '))
            tasksDict.update({doneTaskNumber:{list(tasksDict[doneTaskNumber].keys())[0]:'done'}})
            # print(tasksDict)
            print('Task updated')
        elif choice == 4:
            taskToDelete = int(input('Which Task to delete? '))
            DT = str(list(tasksDict[taskToDelete].keys())[0])
            del tasksDict[taskToDelete]
            print(DT +' Task deleted')
        
        elif choice ==5:
            print('Exiting...')
            break
        else:
            print('Please Enter between 1 to 5')
            continue
  
    except ValueError as ve:
        print('Invalid input:', ve)
        continue
    except KeyError as ke:
        print('Task number does not exist:', ke)
        continue
    


  
















