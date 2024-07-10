import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

def get_winner(player, computer):
    global player_score, computer_score
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

while True:
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    if player_choice == "quit":
        break
    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    result = get_winner(player_choice, computer_choice)
    print(result)
    print(f"Scores -> You: {player_score}, Computer: {computer_score}")