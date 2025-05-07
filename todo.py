import tkinter as tk
from tkinter import messagebox

tasks = []

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "[✔] " if task["done"] else "[ ] "
        task_listbox.insert(tk.END, status + task["task"])

def add_task():
    task_text = task_entry.get().strip()
    if task_text == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return
    tasks.append({"task": task_text, "done": False})
    update_task_list()
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["done"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to mark as done.")

# Create GUI window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Entry for task input
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Add Task", width=10, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Mark Done", width=10, command=mark_done).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Task", width=10, command=delete_task).grid(row=0, column=2, padx=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=20)

# Run the app
root.mainloop()
