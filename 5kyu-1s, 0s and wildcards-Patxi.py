from itertools import product

def possibilities(p):
    p = p.replace('?', '{}')
    return [p.format(*x) for x in product('01', repeat=p.count('{}'))]
