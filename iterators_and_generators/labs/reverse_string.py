def reverse_text(string):
    i = len(string) - 1
    while i > -1:
        yield string[i]
        i -= 1


for char in reverse_text("step"):
    print(char, end='')
