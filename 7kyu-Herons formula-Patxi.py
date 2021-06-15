def heron(a, b, c):
    s = (a + b + c) / 2
    sol = (s * (s - a) * (s - b) * (s - c))**0.5
    return round(sol, 2)