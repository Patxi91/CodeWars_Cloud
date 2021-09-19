def sort_number(a):
    a = sorted(a)
    return [1]+a if a.pop()!=1 else a+[2]
