# Solution 1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_even_digits(num_str):
    return sum(1 for digit in num_str if int(digit) % 2 == 0)

def f(n):
    closest_prime = None
    max_even_digits = 0

    for num in range(n - 1, 1, -1):
        if is_prime(num):
            num_str = str(num)
            even_digits_count = count_even_digits(num_str)

            if even_digits_count > max_even_digits:
                closest_prime = num
                max_even_digits = even_digits_count

    return closest_prime


# Solution 2
def is_prime(num):
    if num % 2 == 0:
        return False
    if num in primes:
        return True
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def f(n):
    global primes
    primes = set()
    max_value = -float('inf')
    max_count = 0
    n -= 1

    while n > 2:
        if is_prime(n):
            even_count = sum(1 for digit in str(n) if int(digit) % 2 == 0)
            if even_count > max_count:
                max_count = even_count
                max_value = n
        n -= 1

    return max_value





