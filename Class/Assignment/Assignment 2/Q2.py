class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book borrowed successfully.")
        else:
            print("No copies available.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print("Book returned successfully.")
        else:
            print("All copies are already in the library.")

    def display_details(self):
        print("Book ID :", self.book_id)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Available Copies :", f"{self.available_copies}/{self.total_copies}")


# Test Scenario
book = Book(101, "Python Programming", "Pavan Kumar", 3)

# 1. Display details
book.display_details()

# 2. Borrow twice
book.borrow_book()
book.borrow_book()

# 3. Display details
book.display_details()

# 4. Borrow twice
book.borrow_book()
book.borrow_book()

# 5. Return once
book.return_book()

# 6. Display details
book.display_details()