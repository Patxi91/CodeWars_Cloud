import math


def square_or_square_root(arr):
    return [x**0.5 if math.isqrt(x)**2 == x else x**2 for x in arr]
