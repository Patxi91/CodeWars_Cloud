def val_point(chessBoard, x, y, max):
    """Biggest possible square from a certain point."""
    for i in range(max - 1):
        s = 0

        width = max - i
        for row in chessBoard[x : x + width]:
            s += sum(row[y : y + width])
            if s == width*width:
                return width
    return None


def count(chessBoard):
    dims = len(chessBoard)
    points = list()
    r = dict()

    for x in range(dims - 1):
        xmax = dims - x
        for y in range(dims - 1):
            max = min(xmax, dims - y)
            biggest = val_point(chessBoard, x, y, max)
            if biggest != None:
                for i in range(2, biggest + 1):
                    if i not in r:
                        r[i] = 1
                    else:
                        r[i] += 1
    return r
