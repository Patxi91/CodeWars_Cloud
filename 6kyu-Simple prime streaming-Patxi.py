def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num**2, limit + 1, num):
                sieve[multiple] = False
    return [num for num in range(2, limit + 1) if sieve[num]]

def generate_prime_sequence(length):
    primes = sieve_of_eratosthenes(length * 20)  # Adjust the factor for sufficient prime numbers
    return ''.join(map(str, primes[:length]))

def solve(a, b):
    sequence = generate_prime_sequence(a + b)
    return sequence[a:a + b]
