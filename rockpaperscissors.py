import tkinter as tk
import random


choices = ['Rock', 'Paper', 'Scissors']
win_streak = 0
highest_streak = 0

# Play game
def play():
    global win_streak, highest_streak
    user_choice = choice_var.get()
    if user_choice == "":
        result_label.config(text="Please choose an option.")
        return
    
    comp_choice = random.choice(choices)
    result = determine_winner(user_choice, comp_choice)
    
    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {comp_choice}")
    
    #Draw
    if result == "Draw":
        result_label.config(text="It's a draw! Try again.")
    #Win
    elif result == "You win!":
        win_streak += 1
        if win_streak > highest_streak:
            highest_streak = win_streak
    #Loss
    elif result == "Computer wins!":
        win_streak = 0
        
    win_streak_label.config(text=f"Win Streak: {win_streak}")
    highest_streak_label.config(text=f"Highest Streak: {highest_streak}")
    result_label.config(text=result)

def determine_winner(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Scissors" and comp == "Paper") or \
         (user == "Paper" and comp == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"


# GUI
root = tk.Tk()
root.geometry("300x350")
root.title("Rock Paper Scissors")

choice_var = tk.StringVar(value="")

# Title
tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

# Radio buttons
for option in choices:
    tk.Radiobutton(root, text=option, variable=choice_var, value=option).pack(anchor='w', padx=30)

# Play button
tk.Button(root, text="Play", command=(play)).pack(pady=10)

# Labels
user_choice = ""
comp_choice = ""

user_label = tk.Label(root, text=f"You chose: {user_choice}")
user_label.pack()

comp_label = tk.Label(root, text=f"Computer chose: {comp_choice}")
comp_label.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=4)

win_streak_label = tk.Label(root, text="Win Streak: 0")
win_streak_label.pack(pady=10)

highest_streak_label = tk.Label(root, text="Highest Streak: 0")
highest_streak_label.pack(pady=10)

root.mainloop()
