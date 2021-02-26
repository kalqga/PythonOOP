n = int(input())


def drawline(i):
    offset = (n - i - 1) * ' '
    content = ('* ' * (i + 1)).strip()
    return f'{offset}{content}'


def upper(num):
    for i in range(num):
        print(drawline(i))


def lower(num):
    for i in range(num - 2, -1, -1):
        print(drawline(i))


upper(n)
lower(n)
