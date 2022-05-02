from itertools import permutations as p

def min_permutation(n):
    if n > 0:
        return min([int(''.join(map(str, sets))) for sets in p(str(n), len(str(n))) if not len(''.join(map(str, sets)))-len((''.join(map(str, sets))).lstrip('0'))])
    elif n == 0:
        return 0
    else:
        n = abs(n)
        return int('-' + str( min([int(''.join(map(str, sets))) for sets in p(str(n), len(str(n))) if not len(''.join(map(str, sets)))-len((''.join(map(str, sets))).lstrip('0'))]) ))
