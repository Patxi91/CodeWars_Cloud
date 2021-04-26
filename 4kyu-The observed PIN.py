def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


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

    merged_list = list(set(list(permutations(digits_s, len(observed))) + list(combinations_with_replacement(digits_s, len(observed)))))
    for tup in range(len(merged_list)):
        merged_list[tup] = join_tup(merged_list[tup])
    return sorted(merged_list)


observed = '369'
sol = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
my_sol = get_pins(observed)




