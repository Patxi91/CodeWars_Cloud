def prescribe(d, a, b):
    # a <= b
    if a == b:
        return b * (d // b)
    elif a > b:
        a, b = b, a

    t = b * (d // b)
    while t + a < d:
        t += a
    if t == d:
        return t

    for th in range(1, d // b + 1):
        n = b * (d // b) - b * th + (a * ((d - (b * (d // b) - b * th)) // a))
        if n > t and n <= d:
            t = n

    return t
