from itertools import permutations


def possible_permutations(nums_list):
    perm = permutations(nums_list)
    for i in perm:
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
