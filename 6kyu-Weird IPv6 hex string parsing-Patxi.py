def parse_IPv6(iPv6):
    arr = [iPv6[x:x+4] for x in range(0, int(len(iPv6)/5)*5+1, 5)]
    sums = []
    for item in arr:
        digits = [x for x in item]
        s = 0
        for digit in digits:
            d = int(str('0x'+digit), 16)
            s += d
        sums.append(s)
    return "".join(str(x) for x in sums)
