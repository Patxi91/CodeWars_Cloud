from collections import Counter


def two_by_two(animals):
    return {k: 2 for (k, v) in dict(Counter(animals)).items() if v >= 2} if animals else False
