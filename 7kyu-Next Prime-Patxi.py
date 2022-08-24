import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

def next_prime(n):
    while True:
        n += 1
        if is_prime(n) and n!=1:
            return n
