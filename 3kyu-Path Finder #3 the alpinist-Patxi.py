import collections


def str2mat(s):
    """Input String to Matrix"""
    mat = s.splitlines()
    for subs in range(len(mat)):
        mat[subs] = list(mat[subs])
    return mat


def path_finder(grid, start=(0, 0)):
    # BFS Preset
    grid_split = str2mat(grid)
    grid_split_back = [''.join(idx for idx in sub) for sub in grid_split]
    width, height = len(grid_split_back[0]), len(grid_split_back)
    flag = False
    min_climbs = 10e6
    # Action
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == (height-1, width-1):  # Goal
            flag = True
            steps = [int(grid_split[index[0]][index[1]]) for index in path]
            levels_climbed = sum(steps[1:-1])-steps[0]+steps[-1]
            if levels_climbed < min_climbs:
                min_climbs = levels_climbed
                min_path = path

            seen.discard((x2, y2))
            x, y = path[-1]

        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    if flag:
        return min_climbs
    else:
        return False



c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"])

f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"])

r_climbs = path_finder(f)


