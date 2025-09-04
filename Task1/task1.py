import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

# Task management functions
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh_listbox():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✖"
        item_text = f"{status} {task['title']} | Priority: {task.get('priority', 'Medium')}"
        if task.get("due_date"):
            item_text += f" | Due: {task['due_date']}"
        listbox.insert(tk.END, item_text)
        # Color coding
        listbox.itemconfig(idx, fg="green" if task["completed"] else "red")

def add_task():
    title = simpledialog.askstring("Task Title", "Enter task title:")
    if not title:
        return
    priority = simpledialog.askstring("Priority", "Enter priority (High/Medium/Low):", initialvalue="Medium")
    due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD) [Optional]:")
    task = {"title": title, "priority": priority, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    refresh_listbox()

def toggle_complete():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a task.")
        return
    idx = selected[0]
    tasks[idx]["completed"] = not tasks[idx]["completed"]
    save_tasks(tasks)
    refresh_listbox()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a task.")
        return
    idx = selected[0]
    del tasks[idx]
    save_tasks(tasks)
    refresh_listbox()

# Main GUI
root = tk.Tk()
root.title("🌟 To-Do List Application 🌟")
root.geometry("600x400")

tasks = load_tasks()

# Listbox with scrollbar
frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=80, height=15, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", command=add_task, width=15, bg="lightblue").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Mark Complete/Incomplete", command=toggle_complete, width=20, bg="lightgreen").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Task", command=delete_task, width=15, bg="lightcoral").grid(row=0, column=2, padx=5)

refresh_listbox()
root.mainloop()
