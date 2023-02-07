def binary(num, length=8):
    return format(num, '0{}b'.format(length + 2))


def f(a: str, b: str) -> int:
    return sum(a[i] != b[i] for i in range(len(a)))


def hamming_distance(a: int, b: int) -> int:
    l = max(len(binary(a)), len(binary(b)))
    return f(binary(a, l), binary(b, l))
