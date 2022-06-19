def is_prime(n):
    # if number is equal to or less than 1, return False
    if n <= 1:
        return False

    for x in range(2, n):
        # if number is divisible by x, return False
        if not n % x:
            return False
    return True
