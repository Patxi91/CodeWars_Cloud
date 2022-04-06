import math


def amount_of_pages(summary):
    sum = 0
    n = 1
    while sum < summary:
        sum += int(math.log10(n)) + 1
        n += 1

    return n - 1 if sum == summary else None
