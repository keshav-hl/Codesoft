import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store contacts
file_name = "contacts.json"

# Load contacts
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        contacts = json.load(f)
else:
    contacts = []

# Save contacts
def save_contacts():
    with open(file_name, "w") as f:
        json.dump(contacts, f, indent=4)

# Add contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    if not name or not phone:
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts()
    messagebox.showinfo("Success", f"Contact '{name}' added!")
    update_contact_list()
    clear_fields()

# Update contact
def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact to update!")
        return
    index = selected[0]
    contacts[index] = {
        "name": name_entry.get().strip(),
        "phone": phone_entry.get().strip(),
        "email": email_entry.get().strip(),
        "address": address_entry.get().strip()
    }
    save_contacts()
    messagebox.showinfo("Success", "Contact updated!")
    update_contact_list()
    clear_fields()

# Delete contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact to delete!")
        return
    index = selected[0]
    name = contacts[index]["name"]
    del contacts[index]
    save_contacts()
    messagebox.showinfo("Success", f"Contact '{name}' deleted!")
    update_contact_list()
    clear_fields()

# Search contacts
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for c in contacts:
        if query in c["name"].lower() or query in c["phone"]:
            contact_list.insert(tk.END, f"{c['name']} | {c['phone']}")

# Display all contacts (only Name & Phone)
def update_contact_list():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']} | {c['phone']}")

# Fill fields when a contact is selected
def on_contact_select(event):
    selected = contact_list.curselection()
    if not selected:
        return
    index = selected[0]
    c = contacts[index]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, c["name"])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, c["phone"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, c["email"])
    address_entry.delete(0, tk.END)
    address_entry.insert(0, c["address"])

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("650x500")
root.configure(bg="#1f1f2f")

# Title
tk.Label(root, text="Contact Book", font=("Helvetica", 24, "bold"), fg="#00ffcc", bg="#1f1f2f").pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#1f1f2f")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name:", bg="#1f1f2f", fg="white").grid(row=0, column=0, sticky="w", padx=5)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Phone:", bg="#1f1f2f", fg="white").grid(row=1, column=0, sticky="w", padx=5)
phone_entry = tk.Entry(input_frame, width=30)
phone_entry.grid(row=1, column=1, padx=5)

tk.Label(input_frame, text="Email:", bg="#1f1f2f", fg="white").grid(row=2, column=0, sticky="w", padx=5)
email_entry = tk.Entry(input_frame, width=30)
email_entry.grid(row=2, column=1, padx=5)

tk.Label(input_frame, text="Address:", bg="#1f1f2f", fg="white").grid(row=3, column=0, sticky="w", padx=5)
address_entry = tk.Entry(input_frame, width=30)
address_entry.grid(row=3, column=1, padx=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1f1f2f")
btn_frame.pack(pady=10)
buttons = [
    ("Add", add_contact, "#00bfff"),
    ("Update", update_contact, "#ffcc00"),
    ("Delete", delete_contact, "#ff4500"),
    ("Clear", clear_fields, "#00ffcc")
]
for text, cmd, color in buttons:
    b = tk.Button(btn_frame, text=text, width=12, bg=color, fg="white", font=("Helvetica", 12, "bold"), command=cmd)
    b.pack(side="left", padx=5, pady=5)
    # Hover effect
    b.bind("<Enter>", lambda e, btn=b: btn.config(bg="white", fg=color))
    b.bind("<Leave>", lambda e, btn=b, c=color: btn.config(bg=c, fg="white"))

# Search Frame
search_frame = tk.Frame(root, bg="#1f1f2f")
search_frame.pack(pady=5)
tk.Label(search_frame, text="Search:", bg="#1f1f2f", fg="white").pack(side="left", padx=5)
search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=5)
tk.Button(search_frame, text="Search", bg="#00ffcc", fg="white", command=search_contact).pack(side="left", padx=5)
tk.Button(search_frame, text="Show All", bg="#00ffcc", fg="white", command=update_contact_list).pack(side="left", padx=5)

# Contact List with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10)
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
contact_list = tk.Listbox(list_frame, width=60, height=15, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
contact_list.pack(side="left", fill="both")
scrollbar.config(command=contact_list.yview)
contact_list.bind("<<ListboxSelect>>", on_contact_select)

update_contact_list()
root.mainloop()
