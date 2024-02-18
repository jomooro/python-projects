import locale
from tabulate import tabulate

def main():
    try:
        principal = float(input("Enter the loan amount: "))
        apr = float(input("Enter the annual interest rate (in percentage): "))
        years = int(input("Enter the loan term in years: "))

        if principal <= 0 or apr < 0 or years <= 0:
            raise ValueError("Please enter valid positive values for the loan amount, interest rate, and loan term.")

        monthly_interest_rate = apr / 1200
        amount_of_months = years * 12
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

        print("\nThe monthly payment for this loan is: {:,.2f}".format(monthly_payment))

        total_amount_paid = monthly_payment * amount_of_months
        print("Total amount paid over the loan term: {:,.2f}".format(total_amount_paid))

        # Optional: Display amortization schedule
        display_amortization_schedule(principal, monthly_interest_rate, amount_of_months, monthly_payment)

    except ValueError as e:
        print("Error:", e)

def display_amortization_schedule(principal, monthly_interest_rate, amount_of_months, monthly_payment):
    print("\nAmortization Schedule:")
    
    # Table headers
    headers = ["Month", "Principal", "Interest", "Remaining Balance"]

    # Table data
    table_data = []
    remaining_balance = principal
    for month in range(1, amount_of_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        # Append data for each row
        table_data.append([month, principal_payment, interest_payment, remaining_balance])

    # Display table using tabulate
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Set the locale for currency formatting (update with your desired locale)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Run the program
main()
