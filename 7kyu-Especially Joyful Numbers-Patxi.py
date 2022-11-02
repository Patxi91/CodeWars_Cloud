def number_joy(n):
    d_s = sum([int(d) for d in str(n)])
    return d_s * int(str(d_s)[::-1]) == n
