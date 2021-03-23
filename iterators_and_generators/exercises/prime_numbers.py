def get_primes(int_list):
    for num in int_list:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
