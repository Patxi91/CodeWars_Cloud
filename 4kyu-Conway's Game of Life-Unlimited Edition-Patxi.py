import numpy as np


def trim_zeros_2D(array, axis=1):
    mask = ~(array==0).all(axis=axis)
    inv_mask = mask[::-1]
    start_idx = np.argmax(mask == True)
    end_idx = len(inv_mask) - np.argmax(inv_mask == True)
    if axis:
        return array[start_idx:end_idx,:]
    else:
        return array[:, start_idx:end_idx]


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
    if generations == 0:
        return cells
    else:
        cells_np = np.array(cells)

        for generation in range(generations):

            add_column = [0] * np.size(cells_np, axis=0)  # Column to be added
            cells_np = np.hstack((np.atleast_2d(add_column).T,  cells_np))  # Add left column
            cells_np = np.hstack((np.atleast_2d(add_column).T, cells_np))  # Add left column
            cells_np = np.hstack((cells_np, np.atleast_2d(add_column).T))  # Add right column
            cells_np = np.hstack((cells_np, np.atleast_2d(add_column).T))  # Add right column

            add_row = [0] * np.size(cells_np, axis=1)  # Row to be added
            cells_np = np.vstack((add_row, add_row,cells_np))  # Upper row
            cells_np = np.vstack((cells_np, add_row, add_row))  # Lower row

            cells_np_sol = np.copy(cells_np)

            for x in range(cells_np.shape[0]):
                for y in range(cells_np.shape[1]):
                    num_neighbours = np.sum(cells_np[x - 1:x + 2, y - 1:y + 2]) - cells_np[x, y]  # Sum of 8 surrounding squares
                    if cells_np[x, y] == 1 and (num_neighbours < 2 or num_neighbours > 3):  # If the cell is alive
                        cells_np_sol[x, y] = 0  # Dies
                    elif cells_np[x, y] == 0 and num_neighbours == 3:  # Otherwise, the cell is dead
                        cells_np_sol[x, y] = 1  # Becomes a live cell

            # Remove zeros
            cells_np_sol = trim_zeros_2D(cells_np_sol, axis=0)
            cells_np_sol = trim_zeros_2D(cells_np_sol, axis=1)

            # Update cells_np for next generation
            cells_np = cells_np_sol

        return cells_np_sol.tolist()

