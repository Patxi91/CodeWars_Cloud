
def sum_consecutives(s):
    p = s[:1]   # final list
    cur = s[0]  # keep track of last seen value

    for i in s[1:]:
        if i == cur:
            p[-1] += i
        else:
            p.append(i)
            cur = i

    return p
