import numpy as np


# O(n^4)
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


# O(n^3)
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


# O(n^3)
def count3(chessBoard):
    r = {}
    n = len(chessBoard)
    arr = np.array(chessBoard, dtype=bool)
    for k in range(2, n+1):
        k_squared = k**2
        sub_arr_shape = (n-k+1, n-k+1, k, k)
        sub_arr_strides = arr.strides + arr.strides
        sub_arr_view = np.lib.stride_tricks.as_strided(arr, shape=sub_arr_shape, strides=sub_arr_strides)
        sub_arr_sum = np.sum(sub_arr_view, axis=(2, 3))
        count = np.count_nonzero(sub_arr_sum == k_squared)
        if count:
            r[k] = count
    return {k:v for k,v in r.items() if v}  # dictionary comprehension to remove keys with zero value


# O(n^3)
def count4(chessBoard):
    r = {}
    n = len(chessBoard)
    arr = np.array(chessBoard, dtype=bool)
    memo = {}  # memo
    for k in range(2, n+1):
        k_squared = k**2
        if k not in memo:
            sub_arr_shape = (n-k+1, n-k+1, k, k)
            sub_arr_strides = arr.strides + arr.strides
            sub_arr_view = np.lib.stride_tricks.as_strided(arr, shape=sub_arr_shape, strides=sub_arr_strides)
            memo[k] = np.sum(sub_arr_view, axis=(2, 3))
        sub_arr_sum = memo[k]
        count = np.count_nonzero(sub_arr_sum == k_squared)
        if count:
            r[k] = count
    return r


# O(n^2)
def count5(chessBoard):
    n = len(chessBoard)
    counts = {}

    # Iterate over all possible squares as the top-left corner
    for i in range(n):
        for j in range(n):
            # Check if the current square is 1
            if chessBoard[i][j] == 1:
                # Iterate over all possible sizes of squares
                for size in range(2, n+1):
                    # Check if the square of the given size is within the board
                    if i+size <= n and j+size <= n:
                        # Check if all the cells within the square of the given size are 1
                        all_ones = True
                        for x in range(i, i+size):
                            for y in range(j, j+size):
                                if chessBoard[x][y] == 0:
                                    all_ones = False
                                    break
                            if not all_ones:
                                break
                        if all_ones:
                            # Increment the count of squares of the given size
                            if size not in counts:
                                counts[size] = 0
                            counts[size] += 1

    return counts


# O(n^2)
def count6(chessBoard):
    n = len(chessBoard)
    count_dict = {}
    arr = np.array(chessBoard)
    for k in range(2, n+1):
        k_squared = k**2
        sub_arr_shape = (n-k+1, n-k+1, k, k)
        sub_arr_strides = arr.strides + arr.strides
        sub_arr_view = np.lib.stride_tricks.as_strided(arr, shape=sub_arr_shape, strides=sub_arr_strides)
        sub_arr_sum = np.sum(sub_arr_view, axis=(2, 3))
        count = np.count_nonzero(sub_arr_sum == k_squared)
        if count:
            count_dict[k] = count
    return count_dict
