def move_zeros(array):
    without_zeros = [num for num in array if num != 0 or isinstance(num, bool)]
    zeros = [num for num in array if num == 0 and not isinstance(num, bool)]
    return without_zeros + zeros
