from itertools import permutations


def sc_perm_comb(num: int) -> int:
    s = str(num)
    n_len = len(s)

    return sum(
        {
            int(''.join(p))
            for i in range(1, n_len + 1)
            for p in set(permutations(s, i))
        }
    )
