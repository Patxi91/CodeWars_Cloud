def decomp(n):
    primes = []
    result = ""

    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)

    for prime in primes:
        power = 0
        num = n

        while num >= prime:
            num //= prime
            power += num

        if power > 1:
            result += str(prime) + "^" + str(power) + " * "
        elif power == 1:
            result += str(prime) + " * "

    return result[:-3]  # Remove the trailing " * "


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
