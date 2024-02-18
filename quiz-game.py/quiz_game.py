import random

def word_guesser():
    words_and_hints = {
        "python": "A programming language",
        "beach": "A sandy shore by the ocean",
        "elephant": "A large mammal with tusks and a trunk",
        "rainbow": "A meteorological phenomenon with colors",
        "mountain": "A large landform that rises prominently above its surroundings",
        "keyboard": "An input device for a computer",
        "astronaut": "A person trained to travel and work in space",
    }

    word = random.choice(list(words_and_hints.keys()))
    hint = words_and_hints[word]

    print("\n***** Welcome to the Word Guesser! *****")
    print("Here's your hint: " + hint)

    attempts = 3 

    while attempts > 0:
        guess = input("\nEnter your guess: ").lower()

        if guess == word:
            print("Congratulations! You guessed the correct word.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left. Try again.")
            else:
                print(f"Sorry, you're out of attempts. The correct word was '{word}'. Better luck next time!")

def number_guesser():
    target_number = random.randint(1, 20)
    attempts = 4

    print("\n***** Welcome to the Number Guesser! *****")
    print("Guess a number between 1 and 20.")

    while attempts > 0:
        guess = int(input("\nEnter your guess: "))

        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left. Try again.")
            else:
                print(f"You're out of attempts.")
                print(f"The correct number was {target_number}. Better luck next time!")

def quiz():
    questions_and_answers = {
        "What is the capital of France?": "Paris",
        "Which planet is known as the Red Planet?": "Mars",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who is the co-founder of Microsoft Corporation?": "Bill Gates",
        "What programming language is commonly used for web development?": "JavaScript",
        "What is the capital city of Japan?": "Japan",
        "What is the popular version control system used by developers?": "Git",
        "Which company is known for its electric cars and sustainable energy solutions?": "Tesla",
        "Elon Musk was born in which country?": "South Africa",
    }

    print("\n***** Welcome to the Quiz! *****")

    score = 0

    for question, correct_answer in questions_and_answers.items():
        print(f"\n{question}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

    print(f"\nQuiz completed! Your score is {score}/{len(questions_and_answers)}.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Word Guesser")
        print("2. Number Guesser")
        print("3. Quiz")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            word_guesser()
        elif choice == "2":
            number_guesser()
        elif choice == "3":
            quiz()
        elif choice == "4":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
