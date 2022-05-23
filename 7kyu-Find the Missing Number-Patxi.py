def missing_no(nums):
    return list(set(range(0, 101)) - set(nums)).pop()
