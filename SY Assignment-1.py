class Library:

    def __init__(self):
        self.books = {}
        self.patrons = []

    # Add a new book
    def add_book(self):
        name = input("Enter book name: ")

        if name in self.books:
            print("Book already exists.")
        else:
            self.books[name] = True
            print("Book added.")

    # Register a patron
    def add_patron(self):
        name = input("Enter patron name: ")

        if name in self.patrons:
            print("Patron already registered.")
        else:
            self.patrons.append(name)
            print("Patron registered.")

    # Borrow a book
    def borrow_book(self):
        patron = input("Enter patron name: ")

        if patron not in self.patrons:
            print("Patron not found.")
            return

        book = input("Enter book name: ")

        if book not in self.books:
            print("Book not found.")
        elif self.books[book]:
            self.books[book] = False
            print(patron, "borrowed", book)
        else:
            print("Book is already borrowed.")

    # Return a book
    def return_book(self):
        book = input("Enter book name: ")

        if book not in self.books:
            print("Book not found.")
        elif self.books[book]:
            print("Book is already in library.")
        else:
            self.books[book] = True
            print("Book returned.")

    # Display books
    def show_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nBooks:")
            for book, status in self.books.items():
                if status:
                    print(book, "- Available")
                else:
                    print(book, "- Borrowed")

    # Display patrons
    def show_patrons(self):
        if len(self.patrons) == 0:
            print("No patrons registered.")
        else:
            print("\nPatrons:")
            for p in self.patrons:
                print(p)


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Books")
    print("6. Show Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.add_patron()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.show_books()

    elif choice == "6":
        library.show_patrons()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
#comments:
===== Library Management System =====
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Show Books
6. Show Patrons
7. Exit
Enter your choice: 3
Enter patron name: jay
Patron not found.

===== Library Management System =====
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Show Books
6. Show Patrons
7. Exit
Enter your choice: 1
Enter book name: cse
Book added.

===== Library Management System =====
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Show Books
6. Show Patrons
7. Exit
