import math


def mixed_fraction(s):
    x = int(s.split('/')[0])
    y = int(s.split('/')[1])
    if y == 0:
        raise ZeroDivisionError
    if x == 0:
        return '0'
    sign = '' if x * y > 0 else '-'
    x, y = abs(x), abs(y)
    a = x // y
    b = x % y
    c = y
    gcd = math.gcd(b, c)
    b = b // gcd
    c = c // gcd
    if a == 0:
        return f"{sign}{b}/{c}" if sign else f"{b}/{c}"
    else:
        if b == 0:
            return f"{sign}{a}"
        else:
            return f"{sign}{a} {b}/{c}"
