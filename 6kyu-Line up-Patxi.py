import itertools


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
