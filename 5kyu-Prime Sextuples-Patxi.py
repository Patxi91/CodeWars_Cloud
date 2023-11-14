def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False

    return {num for num in range(2, limit + 1) if primes[num]}

def find_primes_sextuplet(sum_limit):
    primes = sieve_of_eratosthenes(sum_limit * 2)  # Precompute primes up to 2 * sum_limit
    p = 7  # Start with the first known sextuplet
    while True:
        sextuplet = [p, p + 4, p + 6, p + 10, p + 12, p + 16]
        if sum(sextuplet) > sum_limit and all(num in primes for num in sextuplet):
            return sextuplet
        p += 1
