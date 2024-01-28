def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def total(arr):
    return sum(arr[i] for i in range(len(arr)) if is_prime(i))
