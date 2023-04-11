def to_bcd(n):
    if n < 0:
        sign = "-"
        n = abs(n)
    else:
        sign = ""
    bcd = ""
    while n > 0:
        bcd = "{0:04b} {1}".format(n % 10, bcd)
        n //= 10
    bcd = bcd.strip()
    if not bcd:
        bcd = "0000"
    return sign + bcd
