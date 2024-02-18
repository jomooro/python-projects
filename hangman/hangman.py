import random

def choose_word():
    words = ["python", "hangman", "java", "coding", "test", "happy", "smile", "laugh", "star"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(incorrect_attempts):
    hangman_art = [
        """
         -----
         |   |
             |
             |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ------
        """
    ]
    return hangman_art[incorrect_attempts]

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = len(display_hangman(0))

    while True:
        print(display_hangman(incorrect_attempts))
        print(display_word(word_to_guess, guessed_letters))

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word: {}".format(word_to_guess))
            break

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                incorrect_attempts += 1
                if incorrect_attempts == max_attempts:
                    print(display_hangman(incorrect_attempts))
                    print("Game over! The word was: {}".format(word_to_guess))
                    break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
