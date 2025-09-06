import tkinter as tk
import random
from tkinter import messagebox

# Window setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("450x450")
root.configure(bg="#1f1f2f")

# Initialize scores
user_score = 0
computer_score = 0
winning_score = 20  # Total points to win

options = ["Rock", "Paper", "Scissors"]

# Labels
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 20, "bold"), fg="#00ffcc", bg="#1f1f2f").pack(pady=10)
score_label = tk.Label(root, text=f"You: {user_score} | Computer: {computer_score}", font=("Helvetica", 14), fg="white", bg="#1f1f2f")
score_label.pack(pady=10)
result_label = tk.Label(root, text="", font=("Helvetica", 16), fg="yellow", bg="#1f1f2f")
result_label.pack(pady=10)

def play(user_choice):
    global user_score, computer_score
    
    # Check if game is already over
    if user_score >= winning_score or computer_score >= winning_score:
        return
    
    computer_choice = random.choice(options)
    
    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        user_score += 1
        result = "You win this round!"
    else:
        computer_score += 1
        result = "Computer wins this round!"
    
    # Update display
    result_label.config(text=f"You: {user_choice} | Computer: {computer_choice}\n{result}")
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")
    
    # Check if someone reached winning score
    if user_score >= winning_score:
        messagebox.showinfo("Game Over", f"Congratulations! You won the game {user_score} - {computer_score}")
        reset_game()
    elif computer_score >= winning_score:
        messagebox.showinfo("Game Over", f"Computer wins the game {computer_score} - {user_score}")
        reset_game()

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")
    result_label.config(text="")

# Buttons
button_frame = tk.Frame(root, bg="#1f1f2f")
button_frame.pack(pady=20)
for option in options:
    tk.Button(button_frame, text=option, font=("Helvetica", 14, "bold"), fg="white", bg="#00bfff",
              width=10, command=lambda opt=option: play(opt)).pack(side="left", padx=5)

root.mainloop()
