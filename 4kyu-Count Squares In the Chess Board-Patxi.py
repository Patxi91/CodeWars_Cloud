import numpy as np


def count(chessBoard):
    n = len(chessBoard)
    count_dict = {}

    # Convert the chessBoard to a NumPy array for faster operations
    chessBoard = np.array(chessBoard)

    # Early exit if there are no 1 values on the board
    if not np.any(chessBoard):
        return {}

    # Create a prefix sum array
    prefix_sum = np.zeros((n + 1, n + 1), dtype=int)
    prefix_sum[1:, 1:] = np.cumsum(np.cumsum(chessBoard, axis=0), axis=1)

    for size in range(2, n + 1):
        count = np.sum(prefix_sum[size:, size:] - prefix_sum[:n - size + 1, size:] - prefix_sum[size:, :n - size + 1] + prefix_sum[:n - size + 1, :n - size + 1] == size ** 2)

        if count:
            count_dict[size] = count

    return count_dict
