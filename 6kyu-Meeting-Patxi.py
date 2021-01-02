def meeting(s):
    s = s.upper()
    l = s.split(";")
    ls = []
    lf = []
    for i in range(len(l)):
        ls.append( l[i].split(":")[1] )
        lf.append( l[i].split(":")[0] )
    tz = list(zip(ls, lf))
    tz.sort()
    tzs = ""
    for i in range(len(tz)):
        tzs += "(" + tz[i][0] + ", " + tz[i][1] + ")"
    return tzs
