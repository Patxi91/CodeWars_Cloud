import itertools


def list_depth(l):
    r = 1
    while True:
        flag = True
        for i,j in enumerate(l):
            if isinstance(j, list):
                flag = False
            else:
                l[i] = [j]
        if flag:
            break
        l = list(itertools.chain.from_iterable(l))
        r += 1
    return r
