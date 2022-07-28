import numpy as np


def count_positives_sum_negatives(arr):
    return [np.sum(np.array(arr) > 0, axis=0), np.sum(np.array(arr)[np.array(arr) < 0], axis=0)] if arr else []
