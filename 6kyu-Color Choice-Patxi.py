import math


def checkchoose(m, n):

    if m == 1:
        return 0

    for x in range(1, n + 1):
        combinations = math.comb(n, x)
        if combinations == m:
            return x
    return -1
