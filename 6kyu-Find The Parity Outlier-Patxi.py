def find_outlier(integers):
    if sum(1 if item % 2 else -1 for item in integers) > 0:
        return [item for item in integers if item % 2 == 0][0]
    else:
        return [item for item in integers if item % 2][0]
