from queue import PriorityQueue

MOVEMENT = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_shortest_path(grid, start_node, end_node):
    if not grid:
        return []

    queue = PriorityQueue()
    start = (start_node.position.y, start_node.position.x)
    end = (end_node.position.y, end_node.position.x)
    queue.put((0, (start[0], start[1], 0, [(start[1], start[0])])))

    res = print_grid(grid, start_node, end_node).split("\n")
    visited = set()

    while not queue.empty():
        pos = queue.get()[1]

        if (pos[0], pos[1]) in visited:
            continue

        if (pos[0], pos[1]) == end:
            node_dict = {(j.position.x, j.position.y): j for i in grid for j in i}
            return [node_dict[i] for i in pos[-1]]

        visited.add((pos[0], pos[1]))

        for i, j in MOVEMENT:
            y, x = pos[0] + i, pos[1] + j

            if is_ok(res, y, x) and (y, x) not in visited and res[y][x] in "0E":
                diff = pos[2] + 1 + d_f(y, x, end[0], end[1])
                queue.put((diff, (y, x, pos[2] + 1, pos[-1] + [(x, y)])))

    return []


def d_f(i, j, y, x):
    return abs(i - y) + abs(j - x)


def is_ok(res, y, x):
    if y < 0 or x < 0 or y >= len(res) or x >= len(res[y]):
        return False
    return True
