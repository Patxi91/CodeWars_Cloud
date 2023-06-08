def next_higher(value):
    # Count the number of '1' bits in the input value
    num_ones = bin(value).count('1')

    # Start checking the next number
    next_num = value + 1

    # Keep incrementing the next number until it has the same number of '1' bits
    while bin(next_num).count('1') != num_ones:
        next_num += 1

    return next_num
