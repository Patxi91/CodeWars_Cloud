def hamming_distance(a: str, b: str) -> int:
    return sum(a[i] != b[i] for i in range(len(a)))
