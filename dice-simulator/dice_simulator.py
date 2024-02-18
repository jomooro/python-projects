import random
import time

def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }

    def display_dice(dice):
        print("\n".join(dice_drawing[dice]))

    players = int(input("Enter the number of players: "))
    rounds = int(input("Enter the number of rounds: "))
    scores = [0] * players

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        roll_again = "yes"
        while roll_again.lower() == "yes":
            for player in range(players):
                input(f"\nPlayer {player + 1}, press Enter to roll the dice...")

                for _ in range(3):
                    dice1 = random.randint(1, 6)
                    dice2 = random.randint(1, 6)

                    for _ in range(5):
                        print(f"\rDice 1 rolling: {dice1}", end="")
                        time.sleep(0.1)
                    print("\r", end="")

                    for _ in range(5):
                        print(f"\rDice 2 rolling: {dice2}", end="")
                        time.sleep(0.1)
                    print("\r", end="")

                # Display the final results for both dice
                print(f"\nDice 1 rolled: {dice1}")
                display_dice(dice1)
                
                print(f"\nDice 2 rolled: {dice2}")
                display_dice(dice2)

                total_score = dice1 + dice2
                scores[player] += total_score
                print(f"Player {player + 1} score: {total_score}")

            print("\nCurrent Scores:")
            for player, score in enumerate(scores):
                print(f"Player {player + 1}: {score}")

            roll_again = input("\nRoll again? (yes/no): ")

    print("\nFinal Scores:")
    for player, score in enumerate(scores):
        print(f"Player {player + 1}: {score}")

    max_score = max(scores)
    winners = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    if len(winners) == 1:
        print(f"\nPlayer {winners[0]} is the winner with a score of {max_score}!")
    else:
        print(f"\nIt's a tie! Players {', '.join(map(str, winners))} all have the highest score of {max_score}.")

roll_dice()
