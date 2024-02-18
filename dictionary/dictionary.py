from PyDictionary import PyDictionary

def get_user_input():
    while True:
        word = input("Enter your word (or press Enter to exit): ").strip()
        if not word:
            return None
        else:
            return word

def get_word_meaning(word):
    try:
        dictionary = PyDictionary()
        meaning = dictionary.meaning(word)
        if meaning:
            return meaning
        else:
            raise ValueError(f"No meaning found for the word '{word}'. Please enter another word.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while fetching the meaning: {e}")

def display_meaning(meaning):
    print("\nWord Meaning:")
    print("--------------")
    for part_of_speech, definitions in meaning.items():
        print(f"{part_of_speech.capitalize()}:")
        for i, definition in enumerate(definitions, start=1):
            print(f"{i}. {definition}")
        print()

def main():
    print("Welcome to the Word Dictionary")
    print("--------------------------------------")

    while True:
        word = get_user_input()
        if not word:
            print("Exiting the Word Dictionary. Goodbye!")
            break

        try:
            meaning = get_word_meaning(word)
            display_meaning(meaning)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
