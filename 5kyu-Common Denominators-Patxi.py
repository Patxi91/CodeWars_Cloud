from fractions import gcd
from functools import reduce

def lcmm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers)

def convert_fracts(lst):
    if not lst:
        return []
    denums = tuple(i[1] for i in lst)
    lc = lcmm(*denums)
    return [[i[0]*(lc//i[1]), lc] for i in lst]
