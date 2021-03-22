class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.index = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        num = self.index
        self.index -= 1
        return num


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
