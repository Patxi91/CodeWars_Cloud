def persistence(n):
    product, count = 1, 0
    while len(str(n)) > 1:
        while n != 0:
            rem = n % 10
            product = product * rem
            n = n // 10
        count += 1
        n, product = product, 1
    return count
