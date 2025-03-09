import tkinter as tk

# ----- Data -----
tasks = {"studies": [], "diet": []}

# ----- Window Setup -----
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x500")

# ----- Section Selector (Radio Buttons) -----
section_var = tk.StringVar(value="studies")  # Default section

studies_radio = tk.Radiobutton(root, text="Studies", variable=section_var, value="studies")
studies_radio.pack(pady=5)

diet_radio = tk.Radiobutton(root, text="Diet", variable=section_var, value="diet")
diet_radio.pack(pady=5)

# ----- Task Entry -----
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# ----- Add Task Function -----
def add_task():
    task = task_entry.get()  # Get the text from the entry box
    if not task:
        print("⚠️ No task entered!")
        return
    
    section = section_var.get()  # Get selected section ("studies" or "diet")
    
    if section == "studies":
        studies_listbox.insert(tk.END, task)  # Add to listbox
        tasks["studies"].append(task)         # Add to dictionary
    elif section == "diet":
        diet_listbox.insert(tk.END, task)
        tasks["diet"].append(task)
    
    task_entry.delete(0, tk.END)  # Clear the entry box
    print(f"✅ Added '{task}' to {section}")

# ----- Add Task Button -----
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# ----- Labels and Listboxes for Sections -----
studies_label = tk.Label(root, text="📚 Studies")
studies_label.pack()

studies_listbox = tk.Listbox(root, width=40, height=8)
studies_listbox.pack(pady=5)

diet_label = tk.Label(root, text="🥗 Diet")
diet_label.pack()

diet_listbox = tk.Listbox(root, width=40, height=8)
diet_listbox.pack(pady=5)

# ----- Run the App -----
root.mainloop()

