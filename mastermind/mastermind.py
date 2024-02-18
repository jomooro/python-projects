import random

def run_game():
    code = [random.randint(0, 9) for _ in range(4)]
    correct = False

    print('The hidden password is: ' + ''.join(map(str, code)))

    print('Guess the 4-digit password: between (0-9). You have 5 turns.')

    for turns in range(1, 6): 
        answer = input("Enter 4 digit password: ")

        while len(answer) != 4:
            print("Please enter a 4-digit number.")
            answer = input("Enter 4 digit password: ")

        correct_digits_and_position = sum(code[i] == int(answer[i]) for i in range(4))
        correct_digits_only = sum(int(answer[i]) in code for i in range(4)) - correct_digits_and_position

        print('correct digits in correct place:     ' + str(correct_digits_and_position))
        print('correct digits not in place: ' + str(correct_digits_only))

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You cracked the password!')
            break
        else:
            print('Turns left: ' + str(5 - turns)) 

    print('The password was: ' + str(code))

if __name__ == "__main__":
    run_game()
