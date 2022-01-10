good_numbers = [1, 4, 10, 28, 82, 244, 730, 2188, 6562, 19684, 59050, 177148]

colors = set('RGB')


def simple_solve(g):
    while len(g) > 1:
        g = [a if a == b else (colors - {a, b}).pop() for a, b in zip(g, g[1:])]
    return g[0]


def closest_good_number(n, good_numbers):
    closest = sorted(good_numbers, key=lambda x: abs(x - n))
    for value in closest:
        if value <= n:
            return value


def sides_until_good(g):
    if len(g) < 4:
        return simple_solve(g)

    good_number = closest_good_number(len(g), good_numbers)
    size = len(g) - good_number + 1

    left = g[:size]
    right = g[-size:]

    a = sides_until_good(left)
    b = sides_until_good(right)
    final = simple_solve((a, b))

    return final


def triangle(row):
    return sides_until_good(row)
