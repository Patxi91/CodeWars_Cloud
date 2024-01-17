import math

def simpson(n):
    a, b = 0, math.pi
    h = (b - a) / n

    result = f(a) + f(b)

    # Sum for odd terms
    odd_sum = sum(4 * f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1))

    # Sum for even terms
    even_sum = sum(2 * f(a + 2 * i * h) for i in range(1, n // 2))

    result += odd_sum + even_sum

    return result * h / 3

def f(x):
    return 3/2 * math.sin(x)**3
