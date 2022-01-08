def valid(a):
    
    d = {}
    day_length = len(a[0])
    group_size = len(a[0][0])
    golfers = {g for p in a[0] for g in p}
    
    for day in a:
        if len(day) != day_length:
            return False
        for g in day:
            if len(g) != group_size:
                return False
            for p in g:
                if p not in golfers:
                    return False
                if p not in d:
                    d[p] = set(g)
                else:
                    if len(d[p] & set(g)) > 1:
                        return False
                    else:
                        d[p].add(g)
    
    return True
