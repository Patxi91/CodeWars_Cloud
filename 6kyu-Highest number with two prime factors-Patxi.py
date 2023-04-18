import math


def highest_biPrimefac(p1, p2, nMax):
    max_number = 0
    max_k1 = 0
    max_k2 = 0

    for k1 in range(1, int(math.log(nMax, p1)) + 1):
        for k2 in range(1, int(math.log(nMax, p2)) + 1):
            number = p1 ** k1 * p2 ** k2
            if number <= nMax and number > max_number:
                max_number = number
                max_k1 = k1
                max_k2 = k2

    return [max_number, max_k1, max_k2]
