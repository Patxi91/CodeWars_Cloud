def to_camel_case(t):
    l = [x for x in t]
    e = ['_', '-']

    if len(l) != 0:
        for x in range(len(l)):
            if l[x] in e:
                l[x + 1] = l[x + 1].upper()

    return ''.join([x for x in l if x not in e])
