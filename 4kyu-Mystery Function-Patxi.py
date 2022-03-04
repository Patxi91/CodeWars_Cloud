def mystery(n):
    return int(bin(n^(n >> 1)), 2)

def mystery_inv(n):
    m = n
    while m != 0:
        m >>= 1
        n = n^m
    return n

def name_of_mystery():
    return "Gray code"
