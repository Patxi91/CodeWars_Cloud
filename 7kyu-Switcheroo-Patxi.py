M = {'a':'b', 'b':'a', 'c':'c'}
def switcheroo(s):
    return "".join([M.get(c,c) for c in s])
