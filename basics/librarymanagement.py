class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # By default, the book is not borrowed
    
    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You've borrowed '{self.title}' by {self.author}.")
    
    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"You've returned '{self.title}'.")
class Library:
    def __init__(self):
        self.books = []  # List to store Book objects
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"'{book.title}' by {book.author} - {status}")
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"Sorry, '{title}' is not available in the library.")
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Sorry, '{title}' was not borrowed from this library.")
# Create a Library object
library = Library()

# Add some books to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display available books
library.display_books()

# Borrow a book
library.borrow_book("The Great Gatsby")

# Try to borrow the same book again
library.borrow_book("The Great Gatsby")

# Display available books again
library.display_books()

# Return a book
library.return_book("The Great Gatsby")

# Display available books again
library.display_books()
