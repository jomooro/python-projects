import random

user_wins = 0
computer_wins = 0
max_turns = 3
turn_counter = 0

options = ["rock", "paper", "scissors"]

print("***** Welcome to Rock, Paper, Scissors! *****")

while turn_counter < max_turns:
    user_input = input("Type 'rock', 'paper', or 'scissors' to play, or 'Q' to quit: ").lower()
    
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    
    print("\nYou chose:", user_input)
    print("Computer chose:", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Congratulations! You won this round!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Congratulations! You won this round!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Congratulations! You won this round!")
        user_wins += 1

    else:
        print("Oops! You lost this round.")
        computer_wins += 1

    turn_counter += 1

print("\n***** Game Over! *****")
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Thanks for playing! Goodbye!")
