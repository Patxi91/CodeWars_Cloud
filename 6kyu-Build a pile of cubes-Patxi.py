import math

def find_nb(m):
    n = int(math.sqrt(2 * math.sqrt(m))) - 1
    while ((n * (n + 1)) // 2) ** 2 < m:
        n = n + 1
    return -1 if ((n * (n + 1)) // 2) ** 2 > m else n
