from itertools import permutations as p


def permutations(string):
    return sorted([''.join(perm) for perm in set(list(p(string)))])
