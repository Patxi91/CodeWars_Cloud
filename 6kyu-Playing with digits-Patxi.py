def dig_pow(n, p):
    ds = 0
    sn = str(n)
    for l in sn:
        ds += int(l)**p
        p += 1
    return ds/n if (ds/n).is_integer() else -1
