def multiplication_table(size):
    r = []
    for x in range(1, size+1):
        s = []
        for y in range(1, size+1):
            s.append(x*y)
        r.append(s)
    return r
