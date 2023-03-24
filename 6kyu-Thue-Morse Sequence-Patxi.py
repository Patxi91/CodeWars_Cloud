def thue_morse(n):
    seq = "0"
    while len(seq) < n:
        seq += "".join("01"[(int(c) + 1) % 2] for c in seq)
    return seq[:n]
