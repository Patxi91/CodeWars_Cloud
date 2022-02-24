def compress(s):
    if len(s) is not 0:
        words = s.lower().split(" ")
        res = []
        for x in words:
            if str(x) not in res:
                res.append(x)
        sol = ""
        for x in words:
            sol += str(res.index(x))
        return sol
    else:
        return s
