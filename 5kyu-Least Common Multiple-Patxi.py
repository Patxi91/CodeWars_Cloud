from fractions import gcd
from functools import reduce


def lcm(*args):
    def lcm(a, b):
        return (a * b) // gcd(a, b) if gcd(a, b) != 0 else 0

    return reduce(lcm, args, 1)
