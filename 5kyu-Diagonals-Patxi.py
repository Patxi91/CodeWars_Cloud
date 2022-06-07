import numpy as np


def diagonals(matrix):
    if len(matrix) == 1:
        return matrix[0]

    m = np.matrix(matrix)
    diags = [m[:, ::-1].diagonal(i) for i in range(-m.shape[0] + 1, m.shape[1])]
    diags.extend(m.diagonal(i) for i in range(m.shape[1] - 1, -m.shape[0], -1))

    return [n.tolist()[0] for n in diags]
