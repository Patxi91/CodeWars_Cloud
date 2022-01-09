def prime(num):
    if num == 1 or num == 0:
        return False
    x = 2
    while (x <= num ** 0.5):
        if num % x == 0:
            return False
        x += 1
    return True


def proper_fractions(n):
    if n == 1:
        return 0

    t = 1
    x = n
    y = int(n ** 0.5) + 1

    for i in range(1, y):
        if prime(i):
            if x % i == 0:
                t *= i - 1
                x /= i
            while x % i == 0:
                t *= i
                x /= i
    if x > 1:
        t *= x - 1
    return t
