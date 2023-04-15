import numpy as np

def count(chessBoard):
    r = dict()
    cache = {}
    arr = np.array(chessBoard)
    dims = arr.shape[0]
    for x in range(dims):
        xmax = dims - x
        for y in range(dims):
            max = min(xmax, dims - y)
            for i in range(2, max + 1):
                if (x, y, i) in cache:
                    biggest = cache[(x, y, i)]
                else:
                    sub_arr = arr[x:x+i, y:y+i]
                    s = sub_arr.sum()
                    if s == i*i:
                        biggest = i
                        cache[(x, y, i)] = i
                    else:
                        biggest = None
                        cache[(x, y, i)] = None
                if biggest is not None:
                    if biggest not in r:
                        r[biggest] = 1
                    else:
                        r[biggest] += 1
    return r
