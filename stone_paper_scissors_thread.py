import tkinter as tk
import random
from tkinter import messagebox

# Choices and outcomes
choices = ["Stone", "Paper", "Scissors", "Thread"]
outcome_matrix = {
    ("Stone", "Scissors"): "win",
    ("Stone", "Paper"): "lose",
    ("Stone", "Thread"): "lose",

    ("Paper", "Stone"): "win",
    ("Paper", "Scissors"): "lose",
    ("Paper", "Thread"): "tie",

    ("Scissors", "Paper"): "win",
    ("Scissors", "Stone"): "lose",
    ("Scissors", "Thread"): "win",

    ("Thread", "Stone"): "win",
    ("Thread", "Paper"): "tie",
    ("Thread", "Scissors"): "lose"
}

def get_result(user, comp):
    if user == comp:
        return "tie"
    return outcome_matrix.get((user, comp))

# GUI setup
window = tk.Tk()
window.title("Stone Paper Scissors Thread")
window.geometry("600x550")
window.configure(bg="#f0f5f7")

# Game state
player_score = 0
computer_score = 0
round_count = 0
max_rounds = 5

# UI Elements
title = tk.Label(window, text="Stone Paper Scissors Thread Game", font=("Helvetica", 20, "bold"), bg="#f0f5f7", fg="#333")
title.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 14), bg="#f0f5f7")
score_label.pack(pady=5)

round_label = tk.Label(window, text="Round: 0 / 5", font=("Arial", 12), bg="#f0f5f7")
round_label.pack(pady=5)

result_label = tk.Label(window, text="Choose your option", font=("Arial", 16), bg="#f0f5f7")
result_label.pack(pady=10)

choice_label = tk.Label(window, text="", font=("Arial", 14), bg="#f0f5f7")
choice_label.pack(pady=10)

log_box = tk.Text(window, height=10, width=60, bg="#e8f0fe", font=("Arial", 10))
log_box.pack(pady=10)
log_box.insert(tk.END, "--- Game Log ---\n")
log_box.config(state=tk.DISABLED)

def update_scores(result):
    global player_score, computer_score
    if result == "win":
        player_score += 1
    elif result == "lose":
        computer_score += 1
    score_label.config(text=f"Score - You: {player_score} | Computer: {computer_score}")

def update_log(user, comp, result):
    log_box.config(state=tk.NORMAL)
    log_box.insert(tk.END, f"You: {user} | Computer: {comp} => Result: {result.capitalize()}\n")
    log_box.see(tk.END)
    log_box.config(state=tk.DISABLED)

def play(user_choice):
    global round_count
    if round_count >= max_rounds:
        messagebox.showinfo("Game Over", "Game is finished. Please restart.")
        return
    comp_choice = random.choice(choices)
    result = get_result(user_choice, comp_choice)
    round_count += 1

    round_label.config(text=f"Round: {round_count} / {max_rounds}")
    choice_label.config(text=f"You chose {user_choice} | Computer chose {comp_choice}")

    if result == "tie":
        result_label.config(text="It's a Tie!")
    elif result == "win":
        result_label.config(text="You Win!")
    else:
        result_label.config(text="You Lose!")

    update_scores(result)
    update_log(user_choice, comp_choice, result)

    if round_count == max_rounds:
        winner = "It's a Tie!"
        if player_score > computer_score:
            winner = "You are the Final Winner!"
        elif computer_score > player_score:
            winner = "Computer Wins the Game!"
        messagebox.showinfo("Final Result", winner)

def restart_game():
    global player_score, computer_score, round_count
    player_score = 0
    computer_score = 0
    round_count = 0
    score_label.config(text="Score - You: 0 | Computer: 0")
    round_label.config(text=f"Round: 0 / {max_rounds}")
    result_label.config(text="Choose your option")
    choice_label.config(text="")
    log_box.config(state=tk.NORMAL)
    log_box.delete(1.0, tk.END)
    log_box.insert(tk.END, "--- Game Log ---\n")
    log_box.config(state=tk.DISABLED)

# Buttons Frame
button_frame = tk.Frame(window, bg="#f0f5f7")
button_frame.pack(pady=20)

for choice in choices:
    btn = tk.Button(button_frame, text=choice, font=("Arial", 12, "bold"), width=10, pady=5, bg="#4dc3ff", fg="white",
                    activebackground="#0b85d4", command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=10)

# Control buttons
control_frame = tk.Frame(window, bg="#f0f5f7")
control_frame.pack(pady=10)

restart_btn = tk.Button(control_frame, text="Restart", font=("Arial", 12), command=restart_game, bg="#6fcf97", fg="white")
restart_btn.pack(side=tk.LEFT, padx=10)

exit_btn = tk.Button(control_frame, text="Exit", font=("Arial", 12), command=window.destroy, bg="#ff6f61", fg="white")
exit_btn.pack(side=tk.LEFT, padx=10)

window.mainloop()
