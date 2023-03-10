def sel_reverse(arr, l):
    if l == 0:
        return arr
    n = len(arr)
    i = 0
    while i < n:
        if i + l <= n:
            arr[i:i+l] = reversed(arr[i:i+l])
            i += l
        else:
            arr[i:] = reversed(arr[i:])
            break
    return arr
