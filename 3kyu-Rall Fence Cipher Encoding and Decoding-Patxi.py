from itertools import chain


def f(s, n):
    save = [[] for _ in range(n)]
    l_i = 0
    change = 1
    for c in s:
        save[l_i].append(c)
        if (l_i == n - 1 and change > 0) or (l_i == 0 and change < 0):
            change *= -1
        l_i += change
    return chain.from_iterable(save)


def encode_rail_fence_cipher(string, n):
    return ''.join(f(string, n))


def decode_rail_fence_cipher(string, n):
    save = [''] * len(string)
    for c, i in zip(string, f(range(len(string)), n)):
        save[i] = c
    return ''.join(save)
