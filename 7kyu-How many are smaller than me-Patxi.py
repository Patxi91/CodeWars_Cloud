def smaller(arr):
    r = []
    for i in range(len(arr)):
        r.append(len([n for n in arr[i:] if n < arr[i]]))
    return r
