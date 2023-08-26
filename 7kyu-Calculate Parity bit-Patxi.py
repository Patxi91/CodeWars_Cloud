def check_parity(parity, bin_str):
    count_ones = bin_str.count('1')

    if parity == 'even':
        return count_ones % 2
    elif parity == 'odd':
        return 1 - (count_ones % 2)
