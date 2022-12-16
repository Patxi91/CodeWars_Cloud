def last_survivor(letters, coords):
    a = list(letters)
    for c in coords:
        del a[c]
    return ''.join(a)
