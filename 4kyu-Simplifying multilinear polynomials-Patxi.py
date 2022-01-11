import re


def f_refactor(f):
    output = []
    for k in sorted(f.keys(), key=lambda x: (len(x), x)):
        v = f[k]
        if v == -1:
            output.append("-")
            output.append(k)
        elif v <0:
            output.extend([str(v),k])
        elif v == 1:
            if output:
                output.append("+")
            output.append(k)
        elif v > 1:
            if output:
                output.append("+")
            output.extend([str(v), k])
    return "".join(output)


def f_defactor(value):
    r = re.split('(\d+)', value)
    if len(r) > 1:
        return int(r[1]), r[2]
    else:
        return 1, r[0]

def simplify(poly):
    result2 = []
    for r in poly.split("+"):
        values = r.split("-")
        if values[0]:
            value = values[0]
            result2.append(f_defactor(value))
        for e in values[1:]:
            if e:
                value = e
                n, v = f_defactor(value)
                result2.append((-n, v))
    f = {}
    for n, v in result2:
        v = "".join(sorted(v))
        f[v] = f.get(v, 0) + n
    return f_refactor(f)
