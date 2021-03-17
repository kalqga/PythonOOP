class reverse_iter:

    def __init__(self, it):
        self.it = it
        self.index = len(self.it)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        result = self.it[self.index]
        if self.index < 0:
            raise StopIteration
        return result


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
