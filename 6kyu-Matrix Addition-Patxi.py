import numpy as np


def matrix_addition(a, b):
    a, b = np.array(a), np.array(b)
    return np.add(a, b).tolist()
