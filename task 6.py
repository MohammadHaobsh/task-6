# كلاس الكتاب الأساسي
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.is_available else 'No'}"

# كلاس الرواية (Novel) - يرث من Book
class Novel(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn)
        self.genre = genre

    def __str__(self):
        return super().__str__() + f", Genre: {self.genre}"

# كلاس الكتب غير الروائية (NonFiction) - يرث من Book
class NonFiction(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

    def __str__(self):
        return super().__str__() + f", Subject: {self.subject}"

# كلاس العضو
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {len(self.borrowed_books)}"

# كلاس المكتبة
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def borrow_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn and b.is_available), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book and member:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"Book '{book.title}' borrowed by member '{member.name}'.")
        else:
            print("Book is not available or Member ID not found.")

    def return_book(self, isbn, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
            if book:
                book.is_available = True
                member.borrowed_books.remove(book)
                print(f"Book '{book.title}' returned by member '{member.name}'.")
            else:
                print("Book not found in member's borrowed list.")
        else:
            print("Member ID not found.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)

# اختبار النظام
library = Library()

# إضافة أنواع مختلفة من الكتب
novel1 = Novel("1984", "George Orwell", "123456789", "Dystopian")
non_fiction1 = NonFiction("Sapiens", "Yuval Noah Harari", "987654321", "History")

library.add_book(novel1)
library.add_book(non_fiction1)

# إضافة أعضاء
member1 = Member("Alice", "001")
library.add_member(member1)

# استعارة كتاب
library.borrow_book("123456789", "001")

# عرض الكتب والأعضاء
library.display_books()
library.display_members()

# إرجاع كتاب
library.return_book("123456789", "001")

# عرض الكتب بعد الإرجاع
library.display_books()
