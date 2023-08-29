def next_gen(cells):
    rows = len(cells)
    cols = len(cells[0])
    new_cells = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0

            # Nachbarn zählen (horizontal, vertikal, diagonal)
            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    if (x != i or y != j) and cells[x][y] == 1:
                        live_neighbors += 1

            # Regeln anwenden
            if cells[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_cells[i][j] = 0
                else:
                    new_cells[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_cells[i][j] = 1

    return new_cells
