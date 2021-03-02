from classes_and_instances.exercises.library.library import Library


class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in self.books:
            return f'The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!'


    def return_book(self, author, book_name, library):
        pass

    def info(self):
        pass
