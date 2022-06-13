def stray(arr):
    s = set(arr)
    s.discard(max(set(arr), key = arr.count))
    return list(s)[0]
