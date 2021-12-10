def adjacent_element_product(array):
    return max(tuple(i * j for i, j in zip(array, array[1:])))
