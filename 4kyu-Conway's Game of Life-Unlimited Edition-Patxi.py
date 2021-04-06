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


    pass


start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]





