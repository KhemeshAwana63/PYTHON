"""HERE IS THE COMMAND LINE INTERFACE FOR THE TO DO LIST"""


import json
import os


#making a empyt dictionary to store data
tasks = {"studies":[],"diet":[]}
options = ["add","delete","view","exit"]
file_path = "E:/ME/PYTHON/PROJECTS IN PYTHON/TO_DO_LIST/saved_changes.json"


def AddTask(added_task):
    while True:
        key = input("where do you want to add the task\n studies  \n diet -> ").lower()
        if key not in tasks.keys():
            print("choose the valid option")
            continue
        else:
            tasks[key].append(added_task)
            SaveTask()
            break



def SaveTask():
    global file_path
    with open(file_path,"w") as file:
        json.dump(tasks , file)
    print('tasks added in successfully')



def LoadTask():
    global tasks
    global file_path
    if os.path.exists(file_path):
        if os.stat(file_path).st_size == 0:
            print("empty file detected ..initializing it with default tasks dictionary")
            tasks = {"studies": [], "diet": []}
        else:
            with open(file_path,"r") as file:
               tasks =  json.load(file)
            print('tasks loaded successfully')
    else:
        print("⚠️ No saved file found. Initializing with default tasks dictionary.")
        tasks = {"studies": [], "diet": []}
    


def DeleteTask(deleting_section,deleted_task_index):
    try:
        tasks[deleting_section].pop(deleted_task_index)
        SaveTask()
    except (IndexError , KeyError):
        print("no tasks yet in this section")



def ViewTask():
            print("viewing your tasks")
            for section , tasks_list in tasks.items():
                print(f'\n{section.capitalize()}')
                if tasks_list:
                    for idx , task_detail in enumerate(tasks_list):
                        print(f'{idx} : {task_detail}')
                else:
                    print("no tasks yet")


def main():
    LoadTask()
    while True:
        print("what do you want to do :\n"  
        "add\n"
        "delete\n"
        "view\n"
        "exit")
        inp = input("-> ").lower()
        if inp not in options:
            print("invalid options ...plz chose the correct option")
            continue

        elif inp == "add":  #add function and break call
            added_task = input("put in the task-> ").lower()
            AddTask(added_task)


        elif inp == "delete": #still there is error handling that you would need to do here
            LoadTask()
            deleting_section = input("In which section do you want to delete task").lower()
            if deleting_section not in tasks:
                print("section not found")
                continue

            ViewTask()
            try:
                deleted_task_index = int(input("which task(index) do you want to delete -> "))
                DeleteTask(deleting_section,deleted_task_index)
            except ValueError:
                print("invalid index....plz enter a number")
            

        elif inp == "view":
            ViewTask()
  

        elif inp == "exit":
            print("GOODBYE")
            break

if __name__ == "__main__":
    main()













