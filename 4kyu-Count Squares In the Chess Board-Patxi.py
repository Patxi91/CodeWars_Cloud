def val_point(chessBoard, x, y, max, cache):
    """Biggest possible square from a certain point."""
    if (x, y, max) in cache:
        return cache[(x, y, max)]
    for i in range(max):
        s = 0
        width = max - i
        for row in chessBoard[x:x+width]:
            s += sum(row[y:y+width])
            if s == width*width:
                cache[(x, y, max)] = width
                return width
    cache[(x, y, max)] = None
    return None

def count(chessBoard):
    dims = len(chessBoard)
    points = list()
    r = dict()
    cache = {}
    for x in range(dims):
        xmax = dims - x
        for y in range(dims):
            max = min(xmax, dims - y)
            biggest = val_point(chessBoard, x, y, max, cache)
            if biggest is not None:
                for i in range(2, biggest + 1):
                    if i not in r:
                        r[i] = 1
                    else:
                        r[i] += 1
    return r
