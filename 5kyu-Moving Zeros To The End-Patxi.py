def move_zeros(array):
    sol = [x for x in array if x > 0]
    zeros = [0] * (len(array) - len(sol))
    return sol + zeros
