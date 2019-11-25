def maskify(cc):
    n=len(cc)       
    #solution 2
    mask = ('#' * (n - 4))
    return mask + cc[-4:]
