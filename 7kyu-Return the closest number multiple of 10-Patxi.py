def closest_multiple_10(i):
    i = int(i)
    if i % 10 == 0:
        return i
    for x in range(1, 10):
        if (i + x) % 10 == 0:
            return i + x
        elif (i - x) % 10 == 0:
            return i - x
        else:
            continue
