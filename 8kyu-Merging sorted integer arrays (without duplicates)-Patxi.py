def merge_arrays(first, second):
    L = list(set(first+second))
    L.sort()
    return L
