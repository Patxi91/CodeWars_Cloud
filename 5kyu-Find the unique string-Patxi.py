def find_uniq(arr):
    reduced = [''.join(s.split()) for s in [''.join(list(set(''.join(sorted(a.lower()))))) for a in arr]]
    items = list(set(reduced))
    for item in items:
        if reduced.count(item) == 1:
            return arr[reduced.index(item)]

    return None
