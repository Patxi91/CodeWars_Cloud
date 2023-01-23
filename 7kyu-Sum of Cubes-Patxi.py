def sum_cubes(n):
    if n < 0:
        return
    sum = pow(n * (n + 1) // 2, 2)
    return int(sum)
