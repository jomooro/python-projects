import time
import random

def get_random_text():

    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and challenging.",
        "Python is a powerful and versatile language.",
        "Practice makes perfect.",
        "Type as fast as you can!"
        "Algorithms are the building blocks of software.",
        
    ]
    return random.choice(texts)

def typing_test():
    print("Welcome to the WPM Typing Test!")
    input("Press Enter when you are ready to start...")
    
    text_to_type = get_random_text()
    print("\nType the following text:\n")
    print(text_to_type)
    
    start_time = time.time()
    user_input = input("\nStart typing here: ")
    end_time = time.time()
    
    words_typed = len(user_input.split())
    elapsed_time = end_time - start_time
    words_per_minute = int((words_typed / elapsed_time) * 60)

    print("\nWords per Minute (WPM):", words_per_minute)

if __name__ == "__main__":
    typing_test()

