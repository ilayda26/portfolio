class Book:
    """
    A class representing a book in the library.
    """
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def checked_out(self):
        """
        Marks the book as checked out if it is not already checked out.
        """
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"The book '{self.title}' has been checked out."
        return f"The book '{self.title}' is already checked out."

    def return_book(self):
        """"
        Marks the book as returned if it was checked out.
        """

        if self.is_checked_out:
            self.is_checked_out = False
            return f"The book '{self.title}' has been returned"
        return f"The book '{self.title}' was not checked out."

class Member:
    """
    A class representing a library member.
    """

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Allows the member to borrow a book if it is not already checked out.
        """
        if not book.is_checked_out:
            book.checked_out()
            self.borrowed_books.append(book)
            return f"Member '{self.name}' borrowed '{book.title}'."
        return f"'The book '{book.title}' is already checked out by another member."

    def return_book(self, book):
        """
        Allows the member to return a borrowed book.
        """
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"Member {self.name} returned '{book.title}'."
        return f"'Member '{self.name}' does not have the book '{book.title}'."

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        """
        Adds a book to the library's collection.
        """
        self.books.append(book)
        return f"Book '{book.title}' has been added to the library."

    def add_member(self, member):
        """
        Adds a member to the library's member list.
        """
        self.members.append(member)
        return f"Member '{member.name}' has been added to the library."









