def is_sorted_and_how(arr):
    return 'yes, ascending' if arr == sorted(arr, reverse=False) else 'yes, descending' if arr == sorted(arr, reverse=True) else 'no'
