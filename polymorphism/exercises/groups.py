class Person:
    new_id = -1

    def __init__(self, name, surname):
        Person.new_id += 1
        self.name = name
        self.surname = surname
        self.id = Person.new_id

    def __add__(self, other):
        return Person(self.name, other.surname)

    # def __unicode__(self):
    #     return f"Person {self.id}: {self.name} {self.surname}"

    def __str__(self):
        return f"Person {self.id}: {self.name} {self.surname}"


class Group:

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        li_st = self.people + other.people
        return Group(f"{self.name}&{other.name}", li_st)

    def __getitem__(self, item):
        return self.people[item]

    def __str__(self):
        memb = ', '.join(str(p) for p in self.people)
        return f"Group {self.name} with members {memb}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
