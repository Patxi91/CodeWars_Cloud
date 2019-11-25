from math import pi

def circleArea(radius):
    if not isinstance(radius, (int, float)) or radius <= 0:
        return False
    return round(pi * (radius ** 2), 2)
