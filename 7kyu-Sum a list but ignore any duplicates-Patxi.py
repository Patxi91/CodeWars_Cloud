def sum_no_duplicates(l):
    return sum([e for e in l if l.count(e)==1])
