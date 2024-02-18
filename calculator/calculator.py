import math

def perform_operation(operation, a, b=None):
    if operation == "a":
        result = a + b
        print(f"{a} + {b} = {result}\n")
    elif operation == "b":
        result = a - b
        print(f"{a} - {b} = {result}\n")
    elif operation == "c":
        result = a * b
        print(f"{a} * {b} = {result}\n")
    elif operation == "d":
        result = a / b
        print(f"{a} / {b} = {result}\n")
    elif operation == "e":
        result = math.sqrt(a)
        print(f"Square Root of {a} = {result}\n")
    elif operation == "f":
        result = a ** b
        print(f"{a} ^ {b} = {result}\n")
    elif operation == "g":
        print("Program ended")
        quit()
    else:
        print("Invalid choice. Please choose a valid operation.\n")

while True:
    print("A. Addition\nB. Subtraction\nC. Multiplication\nD. Division\nE. Square Root\nF. Exponentiation\nG. Exit")

    choice = input("Input your choice: ").lower()

    if choice in ["a", "b", "c", "d", "e", "f", "g"]:
        if choice == "g":
            perform_operation(choice, None)
        elif choice in ["a", "b", "c", "d"]:
            a = int(input("Input first number: "))
            b = int(input("Input second number: ")) if choice in ["a", "b", "c", "d"] else None
            perform_operation(choice, a, b)
        elif choice in ["e", "f"]:
            print("Scientific Operation")
            a = int(input("Input base: ")) if choice == "f" else int(input("Input a number: "))
            b = int(input("Input exponent: ")) if choice == "f" else None
            perform_operation(choice, a, b)
    else:
        print("Invalid choice. Please choose a valid operation.\n")
