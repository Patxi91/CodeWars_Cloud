def solution(dig):
    m = max(dig)
    p = []
    for i, d in enumerate(dig[:-4]):
        if d == m:
            p.append(int(dig[i:i+5]))
    return max(p)
