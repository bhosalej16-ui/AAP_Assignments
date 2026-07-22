class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def category(self):
        if self.price >= 500:
            return "Premium"
        else:
            return "Standard"

    def display(self):
        print("Book ID  :", self.book_id)
        print("Title    :", self.title)
        print("Author   :", self.author)
        print("Price    :", self.price)
        print("Category :", self.category())
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\nLibrary Book Records")
        print("=" * 30)
        for book in self.books:
            book.display()


# Main Program
library = Library()

b1 = Book(101, "Python Programming", "Guido van Rossum", 650)
b2 = Book(102, "C Programming", "Dennis Ritchie", 450)
b3 = Book(103, "Java Basics", "James Gosling", 700)

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.display_books()