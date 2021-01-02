def sort_array(source_array):
    odds = iter(sorted(el for el in source_array if el % 2))
    return [next(odds) if el % 2 else el for el in source_array]
