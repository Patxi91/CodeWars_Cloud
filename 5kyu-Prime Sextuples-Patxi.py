def find_primes_sextuplet(sum_limit):
    # Start with the first few known sextuplets
    for p in [7, 97, 16057, 19417, 43777, 1091257, 1615837, 1954357, 2822707, 2839927, 3243337, 3400207, 6005887]:
        if p * 6 + 48 > sum_limit:
            return [p, p + 4, p + 6, p + 10, p + 12, p + 16]

    # Generate additional sextuplets using optimized logic
    p = (sum_limit - 48) // 6 + 1
    if not p % 2:
        if p % 3 == 2:
            p += 3
        else:
            p += 1
    elif p % 2 and p % 3 == 0:
        p += 2

    while 1:
        lst = [p + x for x in (0, 4, 6, 10, 12, 16)]
        for i in range(3, int(lst[-1] ** 0.5) + 1, 2):
            if not all(num % i for num in lst):
                break
        else:
            return lst
        if p % 3 == 2:
            p += 2
        else:
            p += 4
