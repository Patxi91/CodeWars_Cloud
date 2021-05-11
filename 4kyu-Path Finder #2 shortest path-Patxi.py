import numpy as np
import sys

sys.setrecursionlimit(10000)


def isPath(matrix):
    """
    A value of cell 1 means Source.
    A value of cell 2 means Destination.
    A value of cell 3 means Blank cell.
    A value of cell 0 means Blank Wall.
    """

    # Defining visited array to keep
    # track of already visited indexes
    n = len(matrix[0])
    m = len(matrix)
    visited = [[False for x in range(n)] for y in range(m)]

    # Flag to indicate whether the
    # path exists or not
    flag = False

    for i in range(n):
        for j in range(n):

            # If matrix[i][j] is source
            # and it is not visited
            if matrix[i][j] == 1 and not visited[i][j]:

                # Starting from i, j and
                # then finding the path
                path = checkPath(matrix, i, j, visited, 0)
                if path:
                    # If path exists
                    flag = True
                    break
    if flag:
        return path
    else:
        return False


# Method for checking boundaries
def isSafe(i, j, matrix):
    if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
        return True
    return False


# Returns true if there is a
# path from a source(a
# cell with value 1) to a
# destination(a cell with
# value 2)
def checkPath(matrix, i, j, visited, count=0):
    # Checking the boundaries, walls and
    # whether the cell is unvisited
    if isSafe(i, j, matrix) and matrix[i][j] != 0 and not visited[i][j]:

        # Make the cell visited and add to the counter
        visited[i][j] = True
        count += 1

        # If the cell is the required
        # destination then return true
        if matrix[i][j] == 2:
            return count

        # traverse up
        up = checkPath(matrix, i - 1, j, visited, count)

        # If path is found in up
        # direction return true
        if up:
            return True

        # Traverse left
        left = checkPath(matrix, i, j - 1, visited, count)

        # If path is found in left
        # direction return true
        if left:
            return True

        # Traverse down
        down = checkPath(matrix, i + 1, j, visited, count)

        # If path is found in down
        # direction return true
        if down:
            return True

        # Traverse right
        right = checkPath(matrix, i, j + 1, visited)

        # If path is found in right
        # direction return true
        if right:
            return True

    # No path has been found
    return False


def str2mat(s):
    """Input String to Matrix"""
    mat = s.splitlines()
    for subs in range(len(mat)):
        mat[subs] = list(mat[subs])
    return mat


def path_finder(maze):
    if len(maze) <= 2:
        return True

    # Generate matrix
    matrix_np = np.array(str2mat(maze))

    # Presetting matrix
    matrix_np = np.where(matrix_np == '.', 3, 0)
    matrix_np[0][0] = 1  # Source
    n = len(matrix_np[0])
    m = len(matrix_np)
    matrix_np[n - 1][m - 1] = 2  # Destination

    # calling isPath method
    return isPath(matrix_np)










