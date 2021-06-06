import collections

def str2mat(s):
    """Input String to Matrix"""
    mat = s.splitlines()
    for subs in range(len(mat)):
        mat[subs] = list(mat[subs])
    return mat

def path_finder(grid, start=(0, 0)):
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
        if grid_split_back[y][x] == goal:
            flag = True
            return len(path)-1
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid_split_back[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    if not flag:
        return False
