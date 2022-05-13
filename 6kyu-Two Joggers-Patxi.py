import math


def nbr_of_laps(x, y):
    lcm = abs(x*y) // math.gcd(x, y)
    return (lcm/x, lcm/y)
