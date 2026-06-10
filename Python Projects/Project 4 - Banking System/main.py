"""
4. Simple Banking System (Intermediate → Advanced)

Real-world analogy: ATM or bank account

What you'll build:
-Create account 
-Deposit / Withdraw money 
-Check balance 
-Transaction history

Concepts you'll use:
-Dictionaries → account details 
-Lists → transaction history 
-If-else → balance checks 
-Operators → add/subtract money 
-Loops → menu system 

accounts = {
    "1001": {
        "name": "Nikhil",
        "balance": 5000,
        "transactions": [
            "Deposited ₹1000",
            "Withdrawn ₹500"
        ]
    }
}

Advanced touch:
-Prevent overdraft using conditions 
-Store multiple users
"""

account_details = {}
balance_details = {}
transaction_history = []

while True:
    print("\nWelcome to the Banking System Project")
    print("1. Create Account")
    print("2. Deposit/Withdrawal")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        name = input("Enter Name of Account Holder: ")
        acc_no = int(input("Enter Account Number: "))

        if acc_no in account_details:
            print("Account Number already exists.")
        else:
            account_details[acc_no] = name
            balance_details[acc_no] = 0
            print("Account Created Successfully")

    elif choice == 2:
        print(account_details)

        acc_no = int(input("Enter Account Number: "))

        if acc_no not in account_details:
            print("Account Number does not exist.")
        else:
            print("1. Deposit")
            print("2. Withdraw")

            operation = int(input("Enter your Choice: "))

            if operation == 1:
                amount = int(input("Enter amount to deposit: "))
                balance_details[acc_no] += amount

                transaction_history.append(
                    f"Account {acc_no}: Deposited {amount}"
                )

                print("Amount Deposited Successfully")

            elif operation == 2:
                amount = int(input("Enter amount to withdraw: "))

                if amount <= balance_details[acc_no]:
                    balance_details[acc_no] -= amount

                    transaction_history.append(
                        f"Account {acc_no}: Withdrawn {amount}"
                    )

                    print("Amount Withdrawn Successfully")
                else:
                    print("Insufficient Balance")

            else:
                print("Invalid Choice")

    elif choice == 3:
        acc_no = int(input("Enter Account Number: "))

        if acc_no in balance_details:
            print("Current Balance:", balance_details[acc_no])
        else:
            print("Account Number does not exist.")

    elif choice == 4:
        if transaction_history:
            print("\nTransaction History:")
            for transaction in transaction_history:
                print(transaction)
        else:
            print("No transactions found.")

    elif choice == 5:
        print("Thank you for using the Banking System.")
        break

    else:
        print("Enter Valid Choice")

print("\nAccount Details:")
print(account_details)
