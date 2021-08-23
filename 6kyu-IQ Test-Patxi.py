def find_outlier(integers):
    if sum(1 if item % 2 else -1 for item in integers) > 0:
        return integers.index([item for item in integers if item % 2 == 0][0]) + 1
    else:
        return integers.index([item for item in integers if item % 2][0]) + 1


def iq_test(numbers):
    return find_outlier([int(x)for x in numbers.split()])
