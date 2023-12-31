def find_missing_numbers(arr):
    if not arr:
        return []

    missing_numbers = []
    for i in range(arr[0], arr[-1]):
        if i not in arr:
            missing_numbers.append(i)

    return missing_numbers
