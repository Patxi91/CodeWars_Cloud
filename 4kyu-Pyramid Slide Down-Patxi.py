def longest_slide_down(p):
    r = [[0 for j in range(len(p[i]))] for i in range(len(p))]
    r[0][0] = p[0][0]
    for i in range(1, len(p)):
        for j in range(len(p[i])):
            now = p[i][j]
            if 0 < j < len(p[i]) - 1:
                r[i][j] = max(r[i - 1][j] + now, r[i - 1][j - 1] + now)
            elif j == 0:
                r[i][j] = r[i - 1][j] + now
            elif j == len(p[i]) - 1:
                r[i][j] = r[i - 1][j - 1] + now
    return max(r[len(p) - 1])
