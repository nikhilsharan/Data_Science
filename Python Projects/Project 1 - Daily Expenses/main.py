"""
This project is to learn basic concepts like operators variables lists if-else for loop
Adding this multiple line comment to make this project more readable
"""
total_expense = 0

while True: #using while True as we dont know when to stop the loop user will manually do it

    print("Project 1 - Daily Expenses")
    print("From the below option select one\n1.View your daily expenses\n2.Add your daily expenses\n3.Budget exceeded or not\n4.Exit\n")

    choice = int(input("Enter your choice "))

    expenses = []

    if choice == 1:
        if not expenses:
            print("No expense yet")
        else:
            print(expenses)

    elif choice == 2:
        todays_expense = int(input("Enter your expense for today"))
        expenses.append(todays_expense)
        print(expenses)

    elif choice == 3:
        todays_expense = int(input("Enter your expense for today"))
        total_expense = total_expense + todays_expense
        print(total_expense)
        if total_expense > 1000:
            print("Budget is exceeded")
        else:
            print("Expense is under the alloted budget")

    elif choice == 4:
        break








