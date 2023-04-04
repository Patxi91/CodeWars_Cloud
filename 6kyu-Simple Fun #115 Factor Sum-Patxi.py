import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            if is_prime(i):
                factors.append(i)
            n //= i
        else:
            i += 1
    return factors

def factor_sum(n):
    result = n
    while True:
        factors = prime_factors(result)
        new_result = sum(factors)
        if new_result == result:
            return result
        else:
            result = new_result
