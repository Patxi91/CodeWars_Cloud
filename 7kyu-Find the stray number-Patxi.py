def stray(arr):
    s = set(arr).remove(max(set(arr), key = arr.count))
    return s
