def twice_as_old(dad_years_old, son_years_old):
    r = 0
    while True:
        if dad_years_old+r == 2*(son_years_old+r) or dad_years_old-r == 2*(son_years_old-r):
            return r
        else:
            r += 1
