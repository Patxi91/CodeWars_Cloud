def get_mean(arr, x, y):
    if 1 < x <= len(arr) and 1 < y <= len(arr):
        first_mean = sum(arr[:x]) / x
        last_mean = sum(arr[-y:]) / y
        return (first_mean + last_mean) / 2
    else:
        return -1
