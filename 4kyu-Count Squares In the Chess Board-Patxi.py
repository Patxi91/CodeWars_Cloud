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
    r = {}
    n = len(chessBoard)
    arr = np.array(chessBoard, dtype=bool)
    for k in range(2, n+1):
        sub_arr_shape = (n-k+1, n-k+1, k, k)
        sub_arr_strides = arr.strides + arr.strides
        sub_arr_view = np.lib.stride_tricks.as_strided(arr, shape=sub_arr_shape, strides=sub_arr_strides)
        sub_arr_sum = np.sum(sub_arr_view, axis=(2, 3))
        count = np.sum(sub_arr_sum == k**2)
        if count:
            r[k] = count
    return r


