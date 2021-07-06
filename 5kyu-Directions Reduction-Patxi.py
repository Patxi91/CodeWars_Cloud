def dirReduc(arr):
    if not arr:
        return []

    opposites = {   'NORTH': 'SOUTH',
                    'SOUTH': 'NORTH',
                    'EAST': 'WEST',
                    'WEST': 'EAST'
                }

    r = [arr.pop(0)]

    for d in arr:
        if r == [] or opposites[r[-1]] != d:
            r.append(d)
        else:
            r.pop()

    return r
