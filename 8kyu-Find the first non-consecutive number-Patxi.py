def first_non_consecutive(arr):
    prev = arr[0]
    first = None
    for num in arr[1:]:
        if (prev + 1) != num:
            first = num
            break
        prev += 1
    return first
