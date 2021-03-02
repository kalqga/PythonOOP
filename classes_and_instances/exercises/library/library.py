from classes_and_instances.exercises.library.user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        else:
            self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        else:
            self.user_records.remove(user)
            if user in self.rented_books.keys():
                self.rented_books.pop(user)

    def change_username(self, user_id, new_username):
        for users in self.user_records:
            if users.user_id == user_id:
                if users.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    if users.username in self.rented_books.keys():
                        self.rented_books[new_username] = self.rented_books[users.username]
                        del self.rented_books[users.username]
                    else:
                        users.username = new_username
                        return f"Username successfully changed to: {new_username} for userid: {user_id}"

        return f"There is no user with id = {user_id}!"
