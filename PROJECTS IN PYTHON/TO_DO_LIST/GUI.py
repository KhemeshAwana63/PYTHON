import tkinter as tk
tasks = {"studies":[],"diet":[]}


root = tk.Tk()
root.title("khemesh ka jalwa")
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
        print("no task entered")
        return

    #where to append this entry?
    section = section_var.get()

    if section == "studies":
        studies_listbox.insert(tk.END,task)
        tasks["studies"].append(task)
    elif section == "diet":
        Diet_listbox.insert(tk.END,task)
        tasks["diet"].append(task)

    task_entry.delete(0,tk.END)
    print(f'added {task} to {section}')

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
        print("no task selected to delete")
        return
    #putting zero here because beacause jo indices ki tuple hai usme ek hi index hai or wo hai wo wala jo humne choose kar rakha hai to wo tuple me oth place per hai
    index = selected_Indices[0]

    task_to_delete = tasks[section].pop(index)
    list_box.delete(index)

    print(f'deleted {task_to_delete} from {section}')

del_btn = tk.Button(root , text= "delete Task" , command=DeleteTask)
del_btn.pack(pady=5)



studies_lable = tk.Label(root , text="📚 Studies")
studies_lable.pack()

studies_listbox = tk.Listbox(root , width=40 , height=8)
studies_listbox.pack(pady=5)

Diet_lable = tk.Label(root , text="😋 Diet")
Diet_lable.pack()

Diet_listbox = tk.Listbox(root , width=40 , height=8)
Diet_listbox.pack(pady=5)


root.mainloop()