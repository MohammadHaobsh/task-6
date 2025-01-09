class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.is_available else 'No'}"


class Novel(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn)
        self.genre = genre

    def __str__(self):
        return super().__str__() + f", Genre: {self.genre}"


class NonFiction(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

    def __str__(self):
        return super().__str__() + f", Subject: {self.subject}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {len(self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, isbn, member_id):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                for member in self.members:
                    if member.member_id == member_id:
                        book.is_available = False
                        member.borrowed_books.append(book)
                        return f"Book {book.title} borrowed by {member.name}."
        return "Book not available or member not found."

    def return_book(self, isbn, member_id):
        for member in self.members:
            if member.member_id == member_id:
                for book in member.borrowed_books:
                    if book.isbn == isbn:
                        book.is_available = True
                        member.borrowed_books.remove(book)
                        return f"Book {book.title} returned by {member.name}."
        return "Book or member not found."

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)

    def display_members(self):
        if not self.members:
            print("No members in the library.")
        for member in self.members:
            print(member)


def add_book_to_library(library):
    print("\nSelect book type to add:")
    print("1. Novel")
    print("2. NonFiction")
    book_type = input("Enter choice (1/2): ")

    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    if book_type == "1":  # Novel
        genre = input("Enter genre: ")
        novel = Novel(title, author, isbn, genre)
        library.add_book(novel)
        print(f"Novel '{title}' added to the library.")
    elif book_type == "2":  # NonFiction
        subject = input("Enter subject: ")
        non_fiction = NonFiction(title, author, isbn, subject)
        library.add_book(non_fiction)
        print(f"Non-fiction book '{title}' added to the library.")
    else:
        print("Invalid book type!")


def add_member_to_library(library):
    name = input("Enter member name: ")
    member_id = input("Enter member ID: ")
    member = Member(name, member_id)
    library.add_member(member)
    print(f"Member '{name}' added to the library.")


def borrow_book_from_library(library):
    isbn = input("Enter ISBN of the book to borrow: ")
    member_id = input("Enter member ID: ")
    result = library.borrow_book(isbn, member_id)
    print(result)


def return_book_to_library(library):
    isbn = input("Enter ISBN of the book to return: ")
    member_id = input("Enter member ID: ")
    result = library.return_book(isbn, member_id)
    print(result)


def display_books_in_library(library):
    print("\nBooks in library:")
    library.display_books()


def display_members_in_library(library):
    print("\nLibrary members:")
    library.display_members()


def main():
    library = Library()

    options = {
        "1": add_book_to_library,
        "2": add_member_to_library,
        "3": borrow_book_from_library,
        "4": display_books_in_library,
        "5": display_members_in_library,
        "6": return_book_to_library,
        "7": lambda: print("Exiting Library System...") or exit()
    }

    while True:
        print("\nLibrary System")
        print("1. Add book")
        print("2. Add member")
        print("3. Borrow book")
        print("4. Display books")
        print("5. Display members")
        print("6. Return book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        action = options.get(choice)
        if action:
            action(library)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
