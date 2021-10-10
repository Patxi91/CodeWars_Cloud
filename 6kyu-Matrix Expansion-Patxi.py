import numpy as np


def expansion(matrix, n):
    a = np.array(matrix)

    while n > 0:
        a = np.append(a, [np.sum(a, axis=0)], axis=0)  # Append row
        col = np.array([np.sum(a, axis=1)])  # Calculate column
        a = np.concatenate((a, col.T), axis=1)  # Concatenate column
        a[-1][-1] = np.trace(a) - a[-1][-1]  # Correct last diagonal element

    return a


