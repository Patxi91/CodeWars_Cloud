
def is_prime(n):

    # 1 is not a prime number
    if n == 1:
        return False

    factors = 0  # Number of factors in this variable

    for i in range(1, n+1):
        # Check if `i` divides `n`, if yes then we increment the factors
        if n % i == 0:
            factors += 1
    # If total factors are exactly 2
    if factors == 2:
        return True
    return False


def backwards_prime(start, stop):
    sol = []
    for x in range(start, stop+1):
        if is_prime(x)and x != int(str(x)[::-1]) and is_prime(int(str(x)[::-1])):
            sol.append(x)
    return sol


# Test
brp = backwards_prime(2, 100)  # => [13, 17, 31, 37, 71, 73, 79, 97]
