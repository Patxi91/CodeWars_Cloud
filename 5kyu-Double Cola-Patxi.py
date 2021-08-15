def who_is_next(names, r):
    while r > len(names):
        r = (r - len(names) + 1) // 2
    return names[r - 1]
