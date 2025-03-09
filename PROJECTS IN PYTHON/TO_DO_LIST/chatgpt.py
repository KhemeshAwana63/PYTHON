"""HERE IS THE COMMAND LINE INTERFACE FOR THE TO DO LIST"""

import json
import os

# Empty dictionary to store data
tasks = {"studies": [], "diet": []}
options = ["add", "delete", "view", "exit"]

def AddTask(added_task):
    while True:
        key = input("Where do you want to add the task\n studies  \n diet -> ").lower()
        if key not in tasks.keys():
            print("Choose a valid option!")
            continue
        else:
            tasks[key].append(added_task)
            SaveTask()
            print(f'Task "{added_task}" added to {key}!')
            break

def SaveTask():
    with open("E:/ME/PYTHON/PROJECTS IN PYTHON/TO_DO_LIST/saved_changes.json", "w") as file:
        json.dump(tasks, file)
    print('✅ Tasks saved successfully!')

def LoadTask():
    global tasks
    file_path = "E:/ME/PYTHON/PROJECTS IN PYTHON/TO_DO_LIST/saved_changes.json"
    
    if os.path.exists(file_path):
        if os.stat(file_path).st_size == 0:
            print("⚠️ Empty file detected... initializing with default tasks dictionary.")
            tasks = {"studies": [], "diet": []}
        else:
            with open(file_path, "r") as file:
                tasks = json.load(file)
            print("✅ Tasks loaded successfully!")
    else:
        print("⚠️ No saved file found. Initializing with default tasks dictionary.")
        tasks = {"studies": [], "diet": []}

def DeleteTask(deleting_section, deleted_task_index):
    try:
        deleted_task = tasks[deleting_section].pop(deleted_task_index)
        SaveTask()
        print(f'✅ Task "{deleted_task}" deleted from {deleting_section}.')
    except (IndexError, KeyError):
        print("❌ Invalid section or task index!")

def ViewTasks():
    print("\n📝 Viewing your tasks...")
    
    for section, tasks_list in tasks.items():
        print(f'\n📂 {section.capitalize()}')
        if tasks_list:
            for idx, task_detail in enumerate(tasks_list):
                print(f'{idx} : {task_detail}')
        else:
            print("🚫 No tasks yet in this section.")

def main():
    LoadTask()  # Load tasks ONCE at startup!
    
    while True:
        print("\nWhat do you want to do:\n add\n delete\n view\n exit")
        inp = input("-> ").lower()
        
        if inp not in options:
            print("❌ Invalid option... please choose the correct one.")
            continue

        if inp == "add":
            added_task = input("Put in the task -> ").lower()
            AddTask(added_task)

        elif inp == "delete":
            deleting_section = input("In which section do you want to delete a task -> ").lower()
            
            if deleting_section not in tasks:
                print("❌ Section not found!")
                continue

            ViewTasks()  # Show tasks before asking for index
            
            try:
                deleted_task_index = int(input("Which task (index) do you want to delete -> "))
                DeleteTask(deleting_section, deleted_task_index)
            except ValueError:
                print("❌ Invalid index! Please enter a number.")

        elif inp == "view":
            ViewTasks()

        elif inp == "exit":
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
