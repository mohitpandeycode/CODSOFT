import tkinter as tk
from tkinter import messagebox
import random


def get_computer_move():
    moves = ['Rock', 'Paper', 'Scissors']
    return random.choice(moves)

# Function to check the winner and update scores
def check_winner(player_choice, computer_choice):
    # Check for a tie
    if player_choice == computer_choice:
        return "It's a tie!"
    
    # select winner 
    if (player_choice == 'Rock' and computer_choice == 'Scissors') or \
       (player_choice == 'Scissors' and computer_choice == 'Paper') or \
       (player_choice == 'Paper' and computer_choice == 'Rock'):
        global player_score
        player_score += 1
        return "You win!"
    else:
        global computer_score
        computer_score += 1
        return "You lose!"

# function to play a round
def play_round(player_choice):
    computer_choice = get_computer_move()
    result = check_winner(player_choice, computer_choice)
    
    # Update the result text 
    if "win" in result.lower():
        result_label.config(text=f"You picked: {player_choice}\nComputer picked: {computer_choice}\n{result}", fg="green")
    elif "lose" in result.lower():
        result_label.config(text=f"You picked: {player_choice}\nComputer picked: {computer_choice}\n{result}", fg="red")
    else:
        result_label.config(text=f"You picked: {player_choice}\nComputer picked: {computer_choice}\n{result}", fg="blue")

    # Update the score label
    score_label.config(text=f"Score: You - {player_score} | Computer - {computer_score}", fg="darkblue")

# Function to reset the game scores
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="Choose Rock, Paper, or Scissors to start!", fg="black")
    score_label.config(text=f"Score: You - {player_score} | Computer - {computer_score}", fg="darkblue")


def exit_game():
    response = messagebox.askyesno("Exit Game", "Are you sure you want to quit?")
    if response:
        root.quit()

# display scores
player_score = 0
computer_score = 0


root = tk.Tk()
root.title("RPS Game")
root.geometry("500x500")


# Label for the game title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Comic Sans MS", 20, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=15)

# Label for the result of the game
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to start!", font=("Comic Sans MS", 14), bg="#f0f0f0", fg="black")
result_label.pack(pady=20)

# Label for the current score
score_label = tk.Label(root, text=f"Score: You - {player_score} | Computer - {computer_score}", font=("Comic Sans MS", 14, "bold"), bg="#f0f0f0", fg="darkblue")
score_label.pack(pady=10)

# Buttons for the player to make a choice
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=30)

rock_button = tk.Button(button_frame, text="Rock", font=("Comic Sans MS", 12), width=10, bg="#d1e7fd", fg="#0a579a", command=lambda: play_round('Rock'))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Comic Sans MS", 12), width=10, bg="#d4edda", fg="#155d27", command=lambda: play_round('Paper'))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Comic Sans MS", 12), width=10, bg="#f8d7da", fg="#842029", command=lambda: play_round('Scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Buttons for resetting and quitting the game
control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=20)

reset_button = tk.Button(control_frame, text="Reset", font=("Comic Sans MS", 12), bg="#fff3cd", fg="#856404", command=reset_game)
reset_button.grid(row=0, column=0, padx=15)

quit_button = tk.Button(control_frame, text="Quit", font=("Comic Sans MS", 12), bg="#e2e3e5", fg="#41464b", command=exit_game)
quit_button.grid(row=0, column=1, padx=15)

# Start the game loop
root.mainloop()
