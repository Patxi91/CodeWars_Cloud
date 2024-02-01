def how_many_bees(hive):
    if not hive or not hive[0]:
        return 0

    def count_bees(direction, row, col):
        directions = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
        dx, dy = directions[direction]

        if 0 <= row + 2 * dx < rows and 0 <= col + 2 * dy < cols:
            return hive[row][col] == 'b' and hive[row + dx][col + dy] == 'e' and hive[row + 2 * dx][col + 2 * dy] == 'e'
        return False

    bee_count = 0
    rows, cols = len(hive), len(hive[0])

    for i in range(rows):
        for j in range(cols):
            if hive[i][j] == 'b':
                for direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                    bee_count += count_bees(direction, i, j)

    return bee_count