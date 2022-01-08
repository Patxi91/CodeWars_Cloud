import itertools


def permutations(s):
    return sorted(set([''.join(p) for p in itertools.permutations(s)]))


print(permutations('aabb'))