def is_all_possibilities(arr):
    return sorted(arr) == list(range(len(arr))) if arr else False
