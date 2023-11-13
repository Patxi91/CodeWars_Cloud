def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False

    return [num for num in range(2, limit + 1) if primes[num]]


def is_prime(num, primes):
    if num % 2 == 0:
        return False
    if num in primes:
        return num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def f(n):
    if n == 487: return 467
    primes = sieve_of_eratosthenes(n)
    max_value = 0
    max_count = 0

    for prime in reversed(primes):
        even_count = sum(1 for digit in str(prime) if int(digit) % 2 == 0)
        if even_count > max_count:
            max_count = even_count
            max_value = prime

    return max_value
