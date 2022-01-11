def accum(s):
    return '-'.join([str(s[x]*(x+1)).capitalize() for x in range(len(s))])