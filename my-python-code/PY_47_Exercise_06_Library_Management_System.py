# LMS:

# This program demonstrates a Library class with two instance variables:
# 1. no_of_books - to store the number of books.
# 2. books - to store the list of books.
# It includes methods to:
#   - display all books
#   - add a new book
#   - get the total number of books
# Note: The data (books) will not persist after the program stops.


class Library:
    def __init__(self):
        self.books = []                                 # list to store book names
        self.no_of_books = 0                            # count of books

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books = len(self.books)
        print(f'"{book_name}" has been added to the library.')

    def get_no_of_books(self):
        print(f"Total number of books: {self.no_of_books}")


# Create a library object
my_library = Library()

# Add some books
my_library.add_book("Python Basics")
my_library.add_book("Learn JavaScript")
my_library.add_book("Data Structures in Python")

# Show all books
my_library.show_books()

# Get number of books
my_library.get_no_of_books()


# NOTE: Once this program ends, all book data will be lost, because it's stored only in memory (not in any file or database).