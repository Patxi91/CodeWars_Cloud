def first_reverse_try(arr):
    if arr:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr
