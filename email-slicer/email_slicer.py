def get_email():
    while True:
        try:
            email_input = input("Input your email address: ").strip()
            if '@' in email_input and '.' in email_input:
                return email_input
            else:
                raise ValueError("Invalid email address. Please include '@' and '.' in your email.")
        except ValueError as e:
            print(f"Error: {e}")

def email_slicer(email):
    try:
        (username, domain) = email.split("@")
        (domain, extension) = domain.split(".")
        return username, domain, extension
    except ValueError:
        raise ValueError("Invalid email format. Please enter a valid email address.")

def main():
    print("Welcome to the Email Slicer")
    print("--------------------------")

    while True:
        email = get_email()

        try:
            username, domain, extension = email_slicer(email)

            print("\nEmail Details:")
            print("--------------")
            print("Username  :", username)
            print("Domain    :", domain)
            print("Extension :", extension)
        except ValueError as e:
            print(f"Error: {e}")

        another_email = input("\nDo you want to analyze another email? (yes/no): ").lower()
        if another_email != 'yes':
            print("Exiting the Email Slicer. Goodbye!")
            break

if __name__ == "__main__":
    main()
