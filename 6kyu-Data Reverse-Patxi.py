def split_list (big_list, x):
    return [big_list[i:i+x] for i in range(0, len(big_list), x)]


def data_reverse(data):
    return sum(split_list(data, 8)[::-1], [])
