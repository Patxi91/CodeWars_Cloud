from functools import reduce

mul_func = lambda arr: reduce(lambda x, y: x*y, arr)

def sum_prod_diags(matrix):
    return helper(matrix)

def helper(matrix):
    left_diag, right_diag = {}, {}
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            left_diag[j+i] = left_diag.get(j+i, []) + [val]
            right_diag[j-i] = right_diag.get(j-i, []) + [val]
    return sum(mul_func(v) for v in right_diag.values()) - sum(mul_func(v) for v in left_diag.values())
