def race(v1: int, v2: int, g: int):
    m = (g % (v2-v1)) * 60 / (v2-v1)
    h = g/(v2-v1)
    s = (((g % (v2-v1)) * 60) % (v2-v1)) * 60 / (v2-v1)
    return None if v1 >= v2 else [int(h), int(m), int(s)]
