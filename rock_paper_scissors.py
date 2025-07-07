import tkinter as tk
import random

# Scores
player_score = 0
computer_score = 0

# Determine winner
def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "player"
    else:
        return "computer"

# Main game logic
def play(choice):
    global player_score, computer_score

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    winner = get_winner(choice, computer_choice)

    if winner == "player":
        player_score += 1
        result_label.config(text=f"Computer chose: {computer_choice}\nYou Win! 😎", fg="green")
    elif winner == "computer":
        computer_score += 1
        result_label.config(text=f"Computer chose: {computer_choice}\nYou Lose! 😢", fg="red")
    else:
        result_label.config(text=f"Computer chose: {computer_choice}\nIt's a Tie! 🤝", fg="green")

    score_label.config(text=f"You: {player_score}   Computer: {computer_score}")

# Reset function
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="", fg="black")
    score_label.config(text="You: 0   Computer: 0")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.config(bg="white")

# Heading
tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Helvetica", 14, "bold"), bg="white").pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, bg="black", fg="white", command=lambda: play("Rock")).pack(side="left", padx=5)
tk.Button(button_frame, text="Paper", width=10, bg="green", fg="white", command=lambda: play("Paper")).pack(side="left", padx=5)
tk.Button(button_frame, text="Scissors", width=10, bg="red", fg="white", command=lambda: play("Scissors")).pack(side="left", padx=5)

# Result and Score
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="white")
result_label.pack(pady=10)

score_label = tk.Label(root, text="You: 0   Computer: 0", font=("Helvetica", 12, "bold"), bg="white")
score_label.pack(pady=5)

# Reset Button
tk.Button(root, text="Reset Game 🔁", bg="skyblue", command=reset_game).pack(pady=10)

# Run the app
root.mainloop()
