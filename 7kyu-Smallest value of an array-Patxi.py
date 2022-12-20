def find_smallest(numbers,to_return):
    return min(numbers) if to_return=='value' else numbers.index(min(numbers))
