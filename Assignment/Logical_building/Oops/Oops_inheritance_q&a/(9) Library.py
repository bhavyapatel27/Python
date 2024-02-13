class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class Book(LibraryItem):
    def __init__(self, title, author, publication_year, isbn):
        super().__init__(title, author, publication_year)
        self.isbn = isbn

    def borrow(self):
        print(f"Borrowing book: {self}")

    def return1(self):
        print(f"Returning book: {self}")


class Magazine(LibraryItem):
    def __init__(self, title, publication_year, issue_number):
        super().__init__(title, None, publication_year)
        self.issue_number = issue_number

    def read(self):
        print(f"Reading magazine: {self}")


class DVD(LibraryItem):
    def __init__(self, title, publication_year, director):
        super().__init__(title, director, publication_year)

    def watch(self):
        print(f"Watching DVD: {self}")


book1 = Book("Rich dad poor dad", "Robert Kiyosaki and Sharon L. Lechter", 2000,"0-446-67745-0")
print(book1)
book1.borrow()

magazine1 = Magazine("National Geographic", 2023, 12)
magazine1.read()

dvd1 = DVD("Tarzan the wonder Car", 2003, "Mustan")
dvd1.watch()
