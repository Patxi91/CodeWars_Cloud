import numpy as np


def get_generation(cells, generations):
    """
    :param cells: Start generation
    :param generations: Number of evolutions
    :return:

    Conway's Game of Life boundary conditions:
    1.  Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    2.  Any live cell with more than three live neighbours dies, as if by overcrowding.
    3.  Any live cell with two or three live neighbours lives on to the next generation.
    4.  Any dead cell with exactly three live neighbours becomes a live cell.
    """

    cells_np = np.array(cells)

    add_column = [0] * np.size(cells_np, axis=0)  # Column to be added
    cells_np = np.hstack((np.atleast_2d(add_column).T, cells_np))  # Add left column
    cells_np = np.hstack((cells_np, np.atleast_2d(add_column).T))  # Add right column

    add_row = [0] * np.size(cells_np, axis=1)  # Row to be added
    cells_np = np.vstack((add_row, cells_np))  # Upper row
    cells_np = np.vstack((cells_np, add_row))  # Lower row

    for x in range(cells_np.shape[0]):
        for y in range(cells_np.shape[1]):
            num_neighbours = np.sum(cells_np[x - 1:x + 2, y - 1:y + 2]) - cells_np[x, y]  # Sum of 8 surrounding squares

            # If the cell is alive
            if cells_np[x, y] == 1:
                if num_neighbours < 2 or num_neighbours > 3:
                    cells_np[x, y] = 0  # Dies
            # Otherwise, the cell is dead
            elif cells_np[x, y] == 0:
                if num_neighbours == 3:
                    cells_np[x, y] = 1  # Becomes a live cell

    # Remove zeros
    cells_np = np.delete(cells_np, np.argwhere(np.all(cells_np[..., :] == 0, axis=0)), axis=1)
    cells_np = np.delete(cells_np, np.argwhere(np.all(cells_np[:, ...] == 0, axis=1)), axis=0)

    return cells_np


start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]






