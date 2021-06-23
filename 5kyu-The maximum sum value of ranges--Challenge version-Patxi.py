import numpy as np

def max_sum1(a, ranges):
    return max([sum(a[range[0]:range[1]+1]) for range in ranges])

def max_sum2(a, ranges):
    return max([np.array(a)[range(rangei[0], rangei[1]+1)].sum() for rangei in ranges])

def max_sum3(a, ranges):
    a = np.array(a)
    return max([a[range(*rangei)].sum()+a[rangei[1]] for rangei in ranges])

def max_sum4(a, ranges):
    return max([sum(list(map(lambda x: x, a[rangei[0]:rangei[1]+1]))) for rangei in ranges])

a = [1, -2, 3, 4, -5, -4, 3, 2, 1]
ranges = [(1, 3), (0, 4), (6, 8)]
r = max_sum(a, ranges)





