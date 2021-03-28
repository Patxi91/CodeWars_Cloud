import math


# checking for prime
def is_prime(n):
    # checking for up to 1
    if n <= 1:
        return False
    # checking for 2
    elif n == 2:
        return True
    # checking for evens
    elif n > 2 and n % 2 == 0:
        return False
    else:
        # iterating loop till square root of n
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            # checking for factor
            if n % i == 0:
                return False

    return True


def backwards_prime(start, stop):
    sol = []
    for x in range(start, stop + 1):
        if is_prime(x) and x != int(str(x)[::-1]) and is_prime(int(str(x)[::-1])):
            sol.append(x)
    return sol
