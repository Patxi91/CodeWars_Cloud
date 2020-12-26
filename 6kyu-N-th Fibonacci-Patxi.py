def nth_fib(n):
    if n == 1 or n == 2:
        return n-1
    i = 1
    a, b = 0, 1
    while i < n-1:
        i += 1
        a, b = b, a + b
    return b