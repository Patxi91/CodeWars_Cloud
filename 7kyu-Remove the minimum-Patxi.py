def remove_smallest(numbers):
    if not numbers:
        return []
    n = numbers.copy()
    n.remove(min(n))
    return n
