def game(n):
    if n == 0: return [0]
    if n == 1: return [1, 2]
    if n == 2: return [3, 2]
    if n == 3: return [9, 2]
    s, step = 4.5, 3.5
    for i in range(n-3):
        s = s + step
        step += 1.0
    if int(s) == s: return [s]
    else: return [int(str(2*int(s)+1)), 2]
