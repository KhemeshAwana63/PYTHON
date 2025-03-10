import tkinter as tk
import os
import json
from tkinter import messagebox
tasks = {"studies":[],"diet":[]}
file_path = "E:/ME/PYTHON/PROJECTS IN PYTHON/TO_DO_LIST/saved_changes.json"


root = tk.Tk()
root.title("To Do List")
root.geometry("400x500")


section_var = tk.StringVar(value="studies")
studies_radio = tk.Radiobutton(root , text="studies" , variable=section_var,value="studies")
studies_radio.pack(pady=5)
diet_radio = tk.Radiobutton(root , text="diet" , variable=section_var,value="diet")
diet_radio.pack(pady=5)


task_entry = tk.Entry(root,width=30)
task_entry.pack(pady=10)


def AddTask():
    task = task_entry.get()
    if not task:
        messagebox.showinfo("Warning", "No Tasks Entered")
        return

    #where to append this entry?
    section = section_var.get().lower()

    if section == "studies":
        studies_listbox.insert(tk.END,task)
        tasks["studies"].append(task)
    elif section == "diet":
        Diet_listbox.insert(tk.END,task)
        tasks["diet"].append(task)

    task_entry.delete(0,tk.END)
    print(f'added {task} to {section}')
    SaveTask()

add_button = tk.Button(root , text="add task" , command=AddTask)
add_button.pack(pady= 5)


def DeleteTask():
    section = section_var.get()
    if section == "studies":
        list_box = studies_listbox
    else:
        list_box = Diet_listbox

    selected_Indices = list_box.curselection()

    if not selected_Indices:
        messagebox.showinfo("Warning","No Tasks Selected To Delete")
        return
    #putting zero here because beacause jo indices ki tuple hai usme ek hi index hai or wo hai wo wala jo humne choose kar rakha hai to wo tuple me oth place per hai
    index = selected_Indices[0]

    task_to_delete = tasks[section].pop(index)
    list_box.delete(index)

    print(f'deleted {task_to_delete} from {section}')
    SaveTask()

del_btn = tk.Button(root , text= "delete Task" , command=DeleteTask)
del_btn.pack(pady=5)


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

    try:
        studies_listbox.delete(0 , tk.END)
        for task in tasks.get("studies", []):
            studies_listbox.insert(tk.END , task)

        Diet_listbox.delete(0 , tk.END)
        for task in tasks.get("diet", []):
            Diet_listbox.insert(tk.END , task)
    except FileNotFoundError:
        print("No saved file found....starting fresh")



studies_lable = tk.Label(root , text="📚 Studies")
studies_lable.pack()

studies_listbox = tk.Listbox(root , width=40 , height=8)
studies_listbox.pack(pady=5)

Diet_lable = tk.Label(root , text="😋 Diet")
Diet_lable.pack()

Diet_listbox = tk.Listbox(root , width=40 , height=8)
Diet_listbox.pack(pady=5)

#calling load task at the starting of window opening
LoadTask()

#to automatically save the tasks dictionary once the window is closed
root.protocol("WM_DELETE_WINDOW" , lambda :(SaveTask() , root.destroy()))

root.mainloop()