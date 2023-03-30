def digit_sum(n):
    s = str(n)
    total = 0
    for c in s:
        total += int(c)
    return total
