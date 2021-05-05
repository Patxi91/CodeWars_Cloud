import math


def how_many_times_small(a, b):
    arr = [min(a, b), max(a, b)]
    count = 0
    while arr[0] > 0:
        if (arr[1] % arr[0]) == 0:
            count += 1
        arr = [x - 1 for x in arr]
    return count


def how_many_times(a, b):
    if min(a, b) == 0:
        return 0
    if a == b:
        return a
    if min(a, b) == 1:
        return 1
    elif min(a, b) < 100000:
        return how_many_times_small(a, b)

    arr = [min(a, b), max(a, b)]
    diff = arr[1] - arr[0]
    count = 0
    seed = 1

    if arr[0] > diff:
        arr[0] = diff
        arr[1] = diff * 2

    if max(a, b) % min(a, b) == 0:
        count += 1
    elif arr[1] % arr[0] == 0 and diff > 2:
        count += 1

    if diff > 2:
        lim = math.ceil(math.sqrt(diff))
    else:
        lim = math.ceil(math.sqrt(diff)) - 1

    while seed <= math.ceil(math.sqrt(diff)):
        if (diff + seed) % seed == 0:
            count += 1
            if arr[0] > diff / seed > math.ceil(math.sqrt(diff)):
                count += 1
        seed += 1
    return count


def how_many_times2(a, b):
    if a > b: a, b = b, a
    if a <= 0: return -1
    if a == b: return a
    n = b - a
    return sum(1 + (x < n/x <= a) for x in range(1, min(a, int(n**0.5))+1) if not n%x)
