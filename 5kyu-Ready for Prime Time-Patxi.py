def prime(upper):
    primes = []
    for i in range(2, upper + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes
