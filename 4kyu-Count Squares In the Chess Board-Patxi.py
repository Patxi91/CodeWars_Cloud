import numpy as np

def count1(chessBoard):
    r = dict()
    n = len(chessBoard)
    arr = np.array(chessBoard)
    for k in range(2, n+1):
        counts = np.zeros((n-k+1, n-k+1), dtype=int)
        for i in range(n-k+1):
            for j in range(n-k+1):
                sub_arr = arr[i:i+k, j:j+k]
                if np.all(sub_arr):
                    counts[i,j] = 1
        if np.any(counts):
            r[k] = np.sum(counts)
    return r


def count2(chessBoard):
    r = dict()
    n = len(chessBoard)
    arr = np.array(chessBoard)

    for k in range(2, n+1):
        window_shape = (k, k)
        strides = arr.strides
        view_shape = (n-k+1, n-k+1) + window_shape
        view_strides = strides + strides

        # create a view of the chessboard as a set of overlapping windows
        window_view = np.lib.stride_tricks.as_strided(arr, view_shape, view_strides)

        # count the number of squares of size k in each window
        counts = np.count_nonzero(np.all(window_view, axis=(2, 3)))

        if counts > 0:
            r[k] = counts

    return r
