def round_to_next5(n):
    while True:
        if n % 5 == 0:
            return n
        n += 1
