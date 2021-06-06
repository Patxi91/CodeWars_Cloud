import numpy as np
import sys
import collections

sys.setrecursionlimit(10000)

# Globals
global g_counter
g_counter = 10e6

def isPath(matrix):

    # Defining visited array to keep
    # track of already visited indexes
    n = len(matrix[0])
    m = len(matrix)
    visited = [[False for x in range(n)] for y in range(m)]

    # Flag to indicate whether the
    # path exists or not
    flag = False

    for i in range(n):
        if flag:
            break
        for j in range(n):

            # If matrix[i][j] is source
            # and it is not visited
            if matrix[i][j] == 1 and not visited[i][j]:

                # Starting from i, j and
                # then finding the path
                if checkPath(matrix, i, j, visited):
                    # If path exists
                    flag = True
                    break
    if flag:
        return True
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
def checkPath(matrix, i, j, visited, i_counter=-1):
    global g_counter
    # Checking the boundaries, walls and
    # whether the cell is unvisited
    if isSafe(i, j, matrix) and matrix[i][j] != 0 and not visited[i][j]:
        print(i,j,i_counter,g_counter)

        # Make the cell visited
        visited[i][j] = True
        i_counter += 1

        # If the cell is the required destination then return true
        if matrix[i][j] == 2:
            # Check if Path is shortest
            if i_counter < g_counter:
                g_counter = i_counter
            return True

        # traverse up
        up = checkPath(matrix, i - 1, j, visited, i_counter)

        # If path is found in up direction return true
        if up:
            return True

        # Traverse left
        left = checkPath(matrix, i, j - 1, visited, i_counter)

        # If path is found in left
        # direction return true
        if left:
            return True

        # Traverse down
        down = checkPath(matrix, i + 1, j, visited, i_counter)

        # If path is found in down
        # direction return true
        if down:
            return True

        # Traverse right
        right = checkPath(matrix, i, j + 1, visited, i_counter)

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


def bfs_1(grid, start):
    global wall, clear, goal
    global width, height
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def path_finder_1(maze):
    """
    A value of cell 1 means Source.
    A value of cell 2 means Destination.
    A value of cell 3 means Blank cell.
    A value of cell 0 means Blank Wall.
    """

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
    """
        # calling isPath method
        if isPath(matrix_np):
            return g_counter
        else:
            return False
    """
    global wall, clear, goal
    wall, clear, goal = 0, 3, 2
    global width, height
    width, height = n, m
    path = bfs_1(maze, (0, 0))
    return path


def path_finder_2(maze):

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

    # Origin cell to make the search
    x0, y0 = (0, 0)
    targetValue = 2

    # This is the keypoint of the problem: find the positions of the cells containing the searched value
    positions = np.where(matrix_np == targetValue)
    x, y = positions

    dx = abs(x0 - x)  # Horizontal distance
    dy = abs(y0 - y)  # Vertical distance

    # There are different criteria to compute distances
    euclidean_distance = np.sqrt(dx ** 2 + dy ** 2)
    manhattan_distance = abs(dx + dy)
    my_distance = euclidean_distance  # Criterion choice
    min_dist = min(my_distance)

    min_pos = np.argmin(my_distance)  # This method will only return the first occurrence
    min_coords = x[min_pos], y[min_pos]

    if min_coords:
        return sum(min_coords)
    else:
        return False


def bfs_3(grid, start):
    # BFS Preset
    wall, clear, goal = "W", ".", "*"
    grid_split = str2mat(grid)
    grid_split[-1][-1] = '*'
    grid_split_back = [''.join(idx for idx in sub) for sub in grid_split]
    width, height = len(grid_split_back[0]), len(grid_split_back)
    # Action
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def path_finder_3(grid, start=(0, 0)):
    # BFS Preset
    wall, clear, goal = "W", ".", "*"
    grid_split = str2mat(grid)
    grid_split[-1][-1] = '*'
    grid_split_back = [''.join(idx for idx in sub) for sub in grid_split]
    width, height = len(grid_split_back[0]), len(grid_split_back)
    flag = False
    # Action
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            flag = True
            return len(path)
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    if not flag:
        return False


# Driver

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])
r = path_finder_3(d)







#wall, clear, goal = "#", ".", "*"
#width, height = 10, 5
#path = bfs(grid, (5, 2))












