from defining_classes.exercises.todo_list.section import Section


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return f"{new_name}"

    def change_due_date(self, new_date):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return f"{new_date}"

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if comment_number < len(self.comments):
            for i in range(len(self.comments)):
                if i == comment_number:
                    self.comments[i] = new_comment
            result = f"{', '.join(self.comments)}"
            return result
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
