def max_sum(a, ranges):
    return max([sum(a[range[0]:range[1]+1]) for range in ranges])
