import numpy as np


def get_generations(cells, generations):
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
    add_column = [0] * np.size(cells_np, axis=0) # Column to be added
    add_row = [0] * np.size(cells_np, axis=1)  # Row to be added







    # Remove zeros
    a2 = np.delete(a, np.argwhere(np.all(a[..., :] == 0, axis=0)), axis=1)
    a2 = np.delete(a2, np.argwhere(np.all(a[:, ...] == 0, axis=1)), axis=0)

    pass


start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]





