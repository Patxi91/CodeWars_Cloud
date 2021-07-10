import numpy as np
import itertools

def valid_solution(board):
    nums = [i for i in range(1, 10)]
    bn = np.array(board)
    # Small Test 3x3
    if sorted(list(itertools.chain.from_iterable(bn[:3, :3].tolist())))  != nums:
        return False
    # Rows
    for row in np.sort(bn):
        if set(row) != set(nums):
            return False
    # Columns
    for column in np.sort(bn.transpose()):
        if set(column) != set(nums):
            return False
    return True
