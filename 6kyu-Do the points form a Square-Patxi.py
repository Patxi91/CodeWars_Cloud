class Point:

    # Structure of a point in 2D space
    def __init__(self, x, y):
        self.x = x
        self.y = y


# A utility function to find square of
# distance from point 'p' to point 'q'
def distSq(p, q):
    return (p.x - q.x) * (p.x - q.x) + \
           (p.y - q.y) * (p.y - q.y)


# This function returns true if (p1, p2, p3, p4)
# form a square, otherwise false
def isSquare(p1, p2, p3, p4):
    d2 = distSq(p1, p2)  # from p1 to p2
    d3 = distSq(p1, p3)  # from p1 to p3
    d4 = distSq(p1, p4)  # from p1 to p4

    if d2 == 0 or d3 == 0 or d4 == 0:
        return False

    if d2 == d3 and 2 * d2 == d4 and \
            2 * distSq(p2, p4) == distSq(p2, p3):
        return True

    # The below two cases are similar to above case
    if d3 == d4 and 2 * d3 == d2 and \
            2 * distSq(p3, p2) == distSq(p3, p4):
        return True

    if d2 == d4 and 2 * d2 == d3 and \
            2 * distSq(p2, p3) == distSq(p2, p4):
        return True

    return False


def is_square(points):
    if len(points) != 4:
        return False

    p1 = Point(points[0][0], points[0][1])
    p2 = Point(points[1][0], points[1][1])
    p3 = Point(points[2][0], points[2][1])
    p4 = Point(points[3][0], points[3][1])

    if isSquare(p1, p2, p3, p4):
        return True
    else:
        return False
