def solve(a, b):
    # Precompute list of primes less than 100 to check first two digits
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    count = 0
    for i in range(a, b):
        # Check if last two digits of i and i^2 are the same
        if str(i)[-2:] != str(i*i)[-2:]:
            continue

        # Check if first two digits of i and i^2 are prime
        if int(str(i)[:2]) not in primes or int(str(i*i)[:2]) not in primes:
            continue

        count += 1

    return count
