import itertools

# Sol1
def check_hints(colors: list, hints: list) -> list:
    for c in list(itertools.permutations(colors, len(colors))):
        c = list(c)
        flag = False
        for hint in list(set(hints)):
            if not flag:
                hint_s = hint.split()

                if hint_s[-1] == "left":
                    if c.index(hint_s[0]) == 0 or c[c.index(hint_s[0]) - 1] != hint_s[2]:
                        flag = True
                        continue

                if hint_s[-1] == "right":
                    if c.index(hint_s[0]) == len(c) - 1 or c[c.index(hint_s[0]) + 1] != hint_s[2]:
                        flag = True
                        continue

        # If here correct c
        if not flag:
            return c


def line_up(hints):
    l = []
    for hint in hints:
        l.append(hint.split()[0])
        l.append(hint.split()[2])
    colors = list(set(l))

    return check_hints(colors, hints)


# Sol2
def unique(l: list, hints: list) -> list:
    for c in l:
        flag = False
        for hint in list(set(hints)):
            if not flag:
                hint_s = hint.split()

                if hint_s[-1] == "left":
                    if c.index(hint_s[0]) == 0 or c[c.index(hint_s[0]) - 1] != hint_s[2]:
                        flag = True
                        continue

                if hint_s[-1] == "right":
                    if c.index(hint_s[0]) == len(c) - 1 or c[c.index(hint_s[0]) + 1] != hint_s[2]:
                        flag = True
                        continue

        # If here correct c
        if not flag:
            return list(c)


def find(x, y, v):
    return any([x, y] == v[i:i + 2] for i in range(len(v) - 1))


def check_hints(colors: list, hints: list) -> list:
    color1 = hints[0].split()[0]
    if hints[0].split()[-1] == "left":
        color2, color1 = color1, hints[0].split()[2]
    else:
        color2 = hints[0].split()[2]
    c = [comb for comb in list(itertools.permutations(colors, len(colors))) if find(color1, color2, list(comb))]

    for hint in list(set(hints[1:])):
        hint_s = hint.split()
        color1 = hint_s[0]
        if hint_s[-1] == "left":
            color2, color1 = color1, hint_s[2]
        else:
            color2 = hint_s[2]
        c = [comb for comb in c if find(color1, color2, list(comb))]

    # print(c)
    return unique(c, hints)


def line_up(hints):
    colors = []
    for hint in hints:
        colors.append(hint.split()[0])
        colors.append(hint.split()[2])

    return check_hints(list(set(colors)), hints)



