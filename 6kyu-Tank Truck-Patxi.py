import math


def theta(m, r):
    return 2 * math.acos(m/r)


def tankvol(h, d, vt):
    r = d/2
    m = r - h
    l = vt / (math.pi * r**2)
    return math.floor((1/2) * r**2 * (theta(m, r) - math.sin(theta(m, r))) * l)
