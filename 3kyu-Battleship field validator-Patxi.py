def validate_battlefield(field):
    num_cells = 0
    for row in field:
        num_cells += sum(row)
    if num_cells != 20:
        return False

    for row in range(1, 9):
        for col in range(1, 9):
            if field[row][col] == 1:
                if any([field[row - 1][col - 1] == 1,
                        field[row + 1][col - 1] == 1,
                        field[row - 1][col + 1] == 1,
                        field[row + 1][col + 1] == 1]):
                    return False

    SHIPS = {4: 1, 3: 2, 2: 3, 1: 4}
    COUNT = {4: 0, 3: 0, 2: 0, 1: 0}

    for ship in SHIPS.keys():
        for row in range(0, 10):
            cell_count = 0
            for col in range(0, 10):
                if field[row][col] == 1:
                    cell_count += 1
                    if cell_count == ship:
                        if (col != 9) and (field[row][col + 1] == 1):
                            return False
                        COUNT[ship] += 1
                        for cell in range(col, col - ship, -1):
                            field[row][cell] = 0
                else:
                    cell_count = 0
        for col in range(0, 10):
            cell_count = 0
            for row in range(0, 10):
                if field[row][col] == 1:
                    cell_count += 1
                    if cell_count == ship:
                        if (col != 9) and (field[row][col + 1] == 1):
                            return False
                        COUNT[ship] += 1
                        for cell in range(row, row - ship, -1):
                            field[cell][col] = 0
                else:
                    cell_count = 0

    return SHIPS == COUNT
