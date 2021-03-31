def two_sum(arr, target):
    it = 0
    while it < len(arr):
        new_t = target-arr[it]
        if new_t in arr:
            res = [it, arr.index(new_t, it+1, len(arr))]
            res.sort()
            return res
        it += 1
