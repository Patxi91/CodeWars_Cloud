import math


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def solve(x, y):
    count = 0
    for m in range(int(math.log2(y)) + 1):
        for n in range(int(math.log(y, 3)) + 1):
            prime_candidate = 2**m * 3**n + 1
            if x <= prime_candidate <= y and is_prime(prime_candidate):
                count += 1
    return count
