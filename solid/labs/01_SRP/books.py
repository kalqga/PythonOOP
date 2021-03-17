class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:

    def __init__(self):
        self.books = []

    def find_book(self, book_name):
        for book in self.books:
            if book.title == book_name:
                return book

    def add_book(self, book):
        self.books.append(book)


