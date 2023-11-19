def alternate_sort(l):
    sorted_list = sorted(l, key=lambda x: (abs(x), x))
    result = []

    neg_numbers = [num for num in sorted_list if num < 0]
    pos_numbers = [num for num in sorted_list if num >= 0]

    for neg, pos in zip(neg_numbers, pos_numbers):
        result.extend([neg, pos])

    # Handle the case where there are remaining elements in either list
    if len(neg_numbers) > len(pos_numbers):
        result.extend(neg_numbers[len(pos_numbers):])
    elif len(pos_numbers) > len(neg_numbers):
        result.extend(pos_numbers[len(neg_numbers):])

    return result
