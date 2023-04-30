def find_uniq(arr):
    unique_set = set(arr)
    for num in unique_set:
        if arr.count(num) == 1:
            return num
