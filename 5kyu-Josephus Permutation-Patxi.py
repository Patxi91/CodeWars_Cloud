def josephus(items, k):
    if len(items) == 0:
        return []

    if len(items) == 1:
        return [items[0]]

    i = ((k - 1) % len(items))

    return [items[i]] + josephus(items[i + 1:] + items[:i], k)
