import math


def factor_digit(n):
    if n == 0:
        return 1
    else:
        log_sum = sum(math.log10(i) for i in range(1, n+1))
        return math.floor(log_sum) + 1
