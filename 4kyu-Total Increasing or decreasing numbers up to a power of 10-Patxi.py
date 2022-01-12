def total_inc_dec(x):
    y = 1

    for i in range(1, 10):
        y = y * (x + i) // i

    return y * (x + 20) // 10 - x * 10 - 1
