def parse(data):
    r = 0
    ar = []
    for c in data:
        if c == "i":
            r += 1
        if c == "d":
            r -= 1
        if c == "s":
            r = r**2
        if c == "o":
            ar.append(r)
    return ar
