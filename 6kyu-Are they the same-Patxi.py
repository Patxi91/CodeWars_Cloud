def comp(a, b):
    if (a is None and b is None):
        return True
    elif (a is None and b is not None) or  (b is None and a is not None):
        return False
    elif (len(a)==0 and len(b)==0):
        return True
    elif ((a is None or len(a) == 0) and (b is not None and len(b) > 0)) or ((b is None or len(b) == 0) and (a is not None and len(a) > 0)) or (len(a) != len(b)):
        return False
    elif max(a) > max(b):
        x = a
        a = b
        b = x
    x = []
    l_it = len(a)
    for i in range(0, l_it):
        if ( a[0]*a[0] in b ):
            x.append( a[0]*a[0] in b )
            b.remove(a[0]*a[0])
            a.remove(a[0])
        else:
            return False
    return min(x)