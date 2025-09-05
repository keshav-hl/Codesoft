import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Stylish Calculator with History")
root.geometry("400x600")
root.configure(bg="#1f1f2e")

# History panel
history = tk.Text(root, height=6, bg="#2e2e3e", fg="#00ffcc", font=("Helvetica", 14), bd=0)
history.pack(pady=(10,0), padx=10, fill='both')

# Display
display = tk.Entry(root, font=("Digital-7", 36), bg="#1f1f2e", fg="#00ffcc", bd=0, justify='right', insertbackground="#00ffcc")
display.pack(pady=10, padx=10, fill='both')

# Button click function
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expr = display.get()
            result = eval(expr)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            # Add to history
            history.insert(tk.END, f"{expr} = {result}\n")
            history.see(tk.END)  # auto scroll to latest
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)

# Button style function
def create_button(frame, text, bg="#00ffcc"):
    button = tk.Button(frame, text=text, font=("Helvetica", 15), fg="white", bg=bg, bd=0, height=3, width=6, activebackground="#00ff99")
    button.pack(side='left', expand=True, fill='both', padx=5, pady=5)
    button.bind("<Button-1>", click)
    return button

# Buttons layout
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['C','0','=','+']
]

for row in buttons:
    frame = tk.Frame(root, bg="#1f1f2e")
    frame.pack(expand=True, fill='both')
    for b in row:
        # Alternate colors
        color = "#00bfff" if b.isdigit() else "#ff4500"
        create_button(frame, b, bg=color)

root.mainloop()
