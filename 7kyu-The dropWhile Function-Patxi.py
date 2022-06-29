import itertools


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return x % 2 != 0


def drop_while(arr, pred):
    return list(itertools.dropwhile(pred, arr))
