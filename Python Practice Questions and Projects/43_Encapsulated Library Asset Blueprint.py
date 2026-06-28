"""
Create a `Book` class that models properties: `title`, `author`, and `is_checked_out`. Provide a clean custom
string interpretation method `__str__` to output state gracefully, along with instance methods `checkout()`
and `return_book()` that toggle state safely.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print("Book checked out successfully.")
        else:
            print("Book is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"Title: {self.title}\nAuthor: {self.author}\nStatus: {status}"


# Example usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(book)
book.checkout()
print(book)
book.return_book()
print(book)