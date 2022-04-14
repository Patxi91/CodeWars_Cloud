cache = {}

def fibonacci(n: int) -> int:
    # Base Case
    if n == 0 or n == 1:
        return n

    # Check cache
    if n in cache:
        return cache[n]
    else:  # Keep setting cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]
