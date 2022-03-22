import math as m


def count(n):
    return int(m.ceil(m.log(2 * m.pi * n, 10) / 2 + n * m.log(n / m.e, 10)))
