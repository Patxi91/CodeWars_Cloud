def deep_count(a):
    count = 0
    for e in a:
        count += 1
        if isinstance(e, list):
            count += deep_count(e)
    return count
