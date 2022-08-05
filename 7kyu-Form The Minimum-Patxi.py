from itertools import permutations

def min_value(digits):
    return min([int(''.join(map(str, p))) for p in permutations(list(set(digits))) if p[0] != 0])
