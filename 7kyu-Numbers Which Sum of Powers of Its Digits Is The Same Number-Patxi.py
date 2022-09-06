def eq_sum_powdig(hMax, exp):
    r = []
    for i in range(152, hMax+1):
        s = sum([int(str(i)[x])**exp for x in range(len(str(i)))])
        if i == s:
            r.append(i)
    return r
