from inheritance.labs.multiple_inheritance.employee import Employee
from inheritance.labs.multiple_inheritance.person import Person


class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return "teaching..."
