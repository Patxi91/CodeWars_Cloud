# from itertools import product
def product(*args, repeat=1):
    """
    product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    """
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def join_tup(tup):
    res = ''
    for idx in tup:
        res += idx
    return res


def get_pins(observed):

    adj_dig = {1: [1, 2, 4],
               2: [2, 1, 3, 5],
               3: [3, 2, 6],
               4: [4, 1, 5, 7],
               5: [5, 2, 4, 6, 8],
               6: [6, 3, 5, 9],
               7: [7, 4, 8],
               8: [8, 5, 7, 9, 0],
               9: [9, 6, 8],
               0: [0, 8]}

    digits = []
    for i in range(len(observed)):
        digits += adj_dig[int(observed[i])]
    digits = list(dict.fromkeys(digits))  # Remove duplicates
    digits_s = "".join([str(i) for i in digits])

    # Generate all possible combination tuples
    merged_list = list(product(digits_s, repeat=len(observed)))
    # Tuples to strings of integers
    for tup in range(len(merged_list)):
        merged_list[tup] = join_tup(merged_list[tup])

    # Filter not possible answers (keypad layout)
    merged_list_fil = []
    for num in merged_list:
        for d in range(len(observed)):
            if int(num[d]) not in adj_dig[int(observed[d])]:
                merged_list_fil.append(num)  # Not possible variations
                break

    return sorted(set(merged_list).difference(merged_list_fil))
