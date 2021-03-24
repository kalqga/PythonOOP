def vowel_filter(func):
    vowels = {
        'A', 'a', 'E', 'e', 'y', 'Y', 'u', 'U', 'i', 'I', 'O', 'o',
    }

    def wrapper():
        return [el for el in func() if el in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
