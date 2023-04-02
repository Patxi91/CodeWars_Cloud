def rocks(n):
    cost = 0
    digits = 1
    while n > 0:
        if n >= 10 ** digits:
            cost += 9 * 10 ** (digits - 1) * digits
            digits += 1
        else:
            cost += (n - 10 ** (digits - 1) + 1) * digits
            n = 0
    return cost
