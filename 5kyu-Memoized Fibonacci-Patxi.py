cache = {}


def fibonacci(n):
    # Base Case
    if n in [0, 1]:
        return n

    # Check cache
    if n in cache:
        return cache[n]
    else:  # Keep setting cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]
