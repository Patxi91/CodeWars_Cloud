def exp_sum(n):
    s = [1] + n*[0]
    for x in range(1, n+1):
        for y in range(x, n+1):
            s[y] += s[y-x]
    return s[-1]
