def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors_count(n):
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            count += 1
            n //= i
    if n > 1:
        count += 1
    return count

def consec_kprimes(k, arr):
    kprimes_count = 0
    for i in range(len(arr) - 1):
        if prime_factors_count(arr[i]) == k and prime_factors_count(arr[i+1]) == k:
            kprimes_count += 1
    return kprimes_count
