def knight(p1, p2):
    def to_coord(p):
        x = ord(p[0]) - ord('a')
        y = int(p[1]) - 1
        return x, y

    def bfs(start, end, grid, visited, queue):
        if grid[end[0]][end[1]] != 0:
            return grid[end[0]][end[1]]
        if not queue:
            return float('inf')
        x, y = queue.pop(0)
        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8 and not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                grid[new_x][new_y] = grid[x][y] + 1
                if (new_x, new_y) == end:
                    return grid[new_x][new_y]
        return bfs(start, end, grid, visited, queue)

    start = to_coord(p1)
    end = to_coord(p2)
    grid = [[0 for _ in range(8)] for _ in range(8)]
    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = [start]
    visited[start[0]][start[1]] = True
    return bfs(start, end, grid, visited, queue)
