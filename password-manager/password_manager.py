from cryptography.fernet import Fernet

def write_key():
    with open("key.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def view():
    with open('passwords.txt', 'r') as f:
        for line in f:
            user, passw = map(str.strip, line.split("|"))
            print("Account Name:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")

try:
    key = load_key()
except FileNotFoundError:
    write_key()
    key = load_key()

fer = Fernet(key)

while True:
    print("\nWhat would you like to do?")
    print("1. View existing passwords")
    print("2. Add a new password")
    print("q. Quit")

    choice = input("Enter the number or 'q' to quit: ").lower()

    if choice == "q":
        print("Exiting the password manager. Goodbye!")
        break
    elif choice == "1":
        view()
    elif choice == "2":
        add()
    else:
        print("Invalid choice. Please enter a valid option.")
