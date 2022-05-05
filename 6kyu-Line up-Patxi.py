def line_up(hints: list) -> list:
    r = []
    extra = True

    while extra:

        if extra != True:
            hints = extra
            extra = []
        else:
            extra = []

        for hint in hints:
            hint_s = hint.split()
            color1 = hint_s[0]
            color2 = hint_s[2]

            if color1 not in r and color2 not in r:
                if not r:
                    if hint_s[-1] == "left":
                        r.append(color2)
                        r.append(color1)
                    else:
                        r.append(color1)
                        r.append(color2)
                else:
                    extra.append(hint)
                    continue

            elif color1 in r and color2 in r:
                continue

            elif color1 in r or color2 in r:
                if hint_s[-1] == "left":
                    try:
                        r.insert(r.index(color1), color2)  # color1 in r
                    except:
                        r.insert(r.index(color2) + 1, color1)  # color2 in r
                if hint_s[-1] == "right":
                    try:
                        r.insert(r.index(color1) + 1, color2)  # color1 in r
                    except:
                        r.insert(r.index(color2), color1)  # color2 in r

    return r
