def max_and_min(arr1, arr2):
    max_diff = max(max(arr1) - min(arr2), max(arr2) - min(arr1))
    min_diff = float('inf')

    for num1 in arr1:
        for num2 in arr2:
            diff = abs(num1 - num2)
            min_diff = min(min_diff, diff)

    return [max_diff, min_diff]
