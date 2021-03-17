class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.starting = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            pass
        except:
            pass





numbers = take_skip(2, 6)
for number in numbers:
    print(number)