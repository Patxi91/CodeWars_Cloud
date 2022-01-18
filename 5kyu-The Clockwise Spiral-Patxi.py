def create_spiral(n):
    if isinstance(n, int) == False:
        return []

    m = [[1 for x in range(n)] for y in range(n)]
    num = 1
    w = n
    i = 0

    while 0 < w:
        if w == 1:
            m[i][i] = num
        else:
            for j in range(0, w - 1):
                m[i][j + i] = num + j
                m[j + i][i + w - 1] = (w - 1) + num + j
                m[w + i - 1][i + w - 1 - j] = 2 * (w - 1) + num + j
                m[w + i - 1 - j][i] = 3 * (w - 1) + num + j
            num = m[1 + i][i] + 1
        i += 1
        w -= 2

    return m
