import numpy as np


def odd_or_even(arr):
    return "even" if np.sum(np.array(arr)) % 2 == 0 else "odd"
