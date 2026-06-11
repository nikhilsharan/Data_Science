"""
5. Library Management System (Advanced)
Real-world analogy: Real library system

What you'll build:
-Add books 
-Issue / return books 
-Track availability 
-Search books

Concepts you'll use:
-Nested dictionaries → book database 
-Lists → borrowed books 
-Strings → book names, users 
-Loops → search functionality 
-If-else → availability logic 

Example structure:
library = {
  "Python Basics": {"available": True, "issued_to": None}
}

Why this is advanced:
You combine everything and manage complex state.
"""

library = {}
borrow_history = []


def add_book():
    title = input("Enter book title: ")

    if title in library:
        print("Book already exists.")
    else:
        library[title] = {
            "available": True,
            "issued_to": None
        }
        print("Book added successfully.")


def issue_book():
    title = input("Enter book title: ")

    if title not in library:
        print("Book not found.")
        return

    if library[title]["available"]:
        user = input("Enter borrower name: ")

        library[title]["available"] = False
        library[title]["issued_to"] = user

        borrow_history.append({
            "book": title,
            "user": user,
            "action": "Issued"
        })

        print(f"'{title}' issued to {user}.")
    else:
        print(f"Book already issued to {library[title]['issued_to']}.")


def return_book():
    title = input("Enter book title: ")

    if title not in library:
        print("Book not found.")
        return

    if not library[title]["available"]:
        user = library[title]["issued_to"]

        library[title]["available"] = True
        library[title]["issued_to"] = None

        borrow_history.append({
            "book": title,
            "user": user,
            "action": "Returned"
        })

        print(f"'{title}' returned successfully.")
    else:
        print("This book was not issued.")


def search_book():
    keyword = input("Enter book name to search: ").lower()

    found = False

    for title, details in library.items():
        if keyword in title.lower():
            status = "Available" if details["available"] else \
                     f"Issued to {details['issued_to']}"

            print(f"\nBook: {title}")
            print(f"Status: {status}")

            found = True

    if not found:
        print("No matching books found.")


def display_books():
    if not library:
        print("Library is empty.")
        return

    print("\nLibrary Books:")

    for title, details in library.items():
        status = "Available" if details["available"] else \
                 f"Issued to {details['issued_to']}"

        print(f"- {title}: {status}")


def view_history():
    if not borrow_history:
        print("No transactions yet.")
        return

    print("\nBorrow History:")

    for record in borrow_history:
        print(
            f"{record['book']} - "
            f"{record['action']} by {record['user']}"
        )


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display All Books")
    print("6. View Borrow History")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        display_books()

    elif choice == "6":
        view_history()

    elif choice == "7":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Please try again.")