import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_var.get()
    chars = ""
    if upper_var.get():
        chars += string.ascii_uppercase
    if lower_var.get():
        chars += string.ascii_lowercase
    if numbers_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += "!@#$%^&*()"
    if not chars:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Window setup
root = tk.Tk()
root.title("Stylish Password Generator")
root.geometry("500x400")
root.configure(bg="#1f1f2f")

# Title
tk.Label(root, text="Password Generator", font=("Helvetica", 24, "bold"), fg="#00ffcc", bg="#1f1f2f").pack(pady=20)

# Options Frame
frame = tk.Frame(root, bg="#1f1f2f")
frame.pack(pady=10)

length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Label(frame, text="Length:", fg="white", bg="#1f1f2f", font=("Helvetica", 14)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Spinbox(frame, from_=4, to=32, textvariable=length_var, width=5, font=("Helvetica", 14)).grid(row=0, column=1, padx=5, pady=5)

tk.Checkbutton(frame, text="Uppercase", variable=upper_var, fg="white", bg="#1f1f2f", selectcolor="#1f1f2f", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
tk.Checkbutton(frame, text="Lowercase", variable=lower_var, fg="white", bg="#1f1f2f", selectcolor="#1f1f2f", font=("Helvetica", 12)).grid(row=1, column=1, padx=5, pady=5)
tk.Checkbutton(frame, text="Numbers", variable=numbers_var, fg="white", bg="#1f1f2f", selectcolor="#1f1f2f", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5)
tk.Checkbutton(frame, text="Symbols", variable=symbols_var, fg="white", bg="#1f1f2f", selectcolor="#1f1f2f", font=("Helvetica", 12)).grid(row=2, column=1, padx=5, pady=5)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 16, "bold"), bg="#00ffcc", fg="#1f1f2f", bd=0, height=2).pack(pady=20)

# Password Display
password_entry = tk.Entry(root, font=("Helvetica", 18), width=30, justify="center", bd=0)
password_entry.pack(pady=10)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Helvetica", 14), bg="#ff69b4", fg="white", bd=0, height=2).pack(pady=10)

root.mainloop()
