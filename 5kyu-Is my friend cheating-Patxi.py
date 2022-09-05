def remov_nb(n):
    equal = []
    sum = n * (1 + n) / 2
    for i in range(1, 1+n):
        j = (sum-i)/(i+1)
        if j == int(j) and j <= n+1 and j != i:
            equal.append((int(i), int(j)))
    return equal
