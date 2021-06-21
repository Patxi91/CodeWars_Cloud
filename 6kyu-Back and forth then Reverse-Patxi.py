
def arrange1(s):
    t = []
    sc = s.copy()
    while sc:
        try:
            t.append(sc[0])
            t.append(sc[-1])
            sc = [x for x in reversed(sc[1:-1])]
        except:
            break
    return t

def arrange2(s):
    t = []
    sc = s.copy()
    while sc:
        try:
            t.append(sc[0])
            t.append(sc[-1])
            sc = sc[::-1]
        except:
            break
    return t

import math
def arrange3(s):
    t = []
    sc = [x for x in s]
    for seq in range(math.ceil(len(s)/2)-1):
        a, *b, c = sc
        t.extend((a, c))
        sc = b[::-1]
    t.extend(sc)
    return t


def arrange(s):
    if len(s)<2:
        return s
    else:
        t = []
        a, *b, c = s
        t.extend((a, c))
        while len(b) > 1:
            a, *b, c = b[::-1]
            t.extend((a, c))
        t.extend(b)
        return t




r = arrange([4, 3, 2])




