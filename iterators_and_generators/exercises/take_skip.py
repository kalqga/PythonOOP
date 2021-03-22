class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index / self.step >= self.count:
            raise StopIteration
        num = self.index
        self.index += self.step
        return num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
