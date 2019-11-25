from math import pi

def circleArea(r):
    if not isinstance(r, (int, float)) or r <= 0:
        return False
    return round(pi * (r ** 2), 2)
