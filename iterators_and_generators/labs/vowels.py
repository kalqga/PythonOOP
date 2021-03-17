class vowels:
    VOWELS = [
        "a",
        "A",
        "E",
        "e",
        "I",
        "i",
        "U",
        "u",
        "O",
        "o",
        "y",
        "Y",
    ]

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.string[self.index] in vowels.VOWELS:
                result = self.string[self.index]
                self.index += 1
                return result
            else:
                self.index += 1
                return self.__next__()
        except IndexError:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
