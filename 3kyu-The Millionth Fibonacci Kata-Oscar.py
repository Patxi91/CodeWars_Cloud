
cache = {}
def fib(n):
    if n == 0 or n==1:
        return n

    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1)+fib(n-2)

    return cache[n]
