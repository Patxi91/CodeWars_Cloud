def shifted_diff(first, second):
    if len(first) != len(second):
        return -1

    if first == second:
        return 0

    for i in range(len(first)):
        rotated = first[i:] + first[:i]
        if rotated == second:
            return len(first) - i

    return -1
