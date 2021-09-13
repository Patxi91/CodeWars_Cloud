from itertools import combinations
import math


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


def area(c):
    a = distance(c[0], c[1])
    b = distance(c[0], c[2])
    c = distance(c[1], c[2])
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def maxmin_areas(points):
    r = [0, 1e9]
    for c in combinations(points, 3):
        a = area(c)
        if isinstance(a, complex) or a < 0.1:
            continue
        if a > r[0]:
            r[0] = a
            if r[1] > r[0]:
                r[1] = r[0]
        elif a < r[1] and a != 0:
            r[1] = a
    return (int(r[0]) if int(r[0]) == round(r[0], 2) else round(r[0], 2),
            int(r[1]) if int(r[1]) == round(r[1], 2) else round(r[1], 2))
