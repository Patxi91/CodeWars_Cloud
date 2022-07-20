def solve(s):
    if not s:
        return ''
    print(s)
    s = s.replace("[backspace]", "§")
    p = ""
    last = ""

    for i in range(len(s)):
        print(i, len(s))
        if s[i] == "§" and i < len(s) - 1 and s[i + 1] != "*":
            p = p[:-1]
        elif s[i] == "§" and i < len(s) - 1 and s[i + 1] == "*" and s[i + 2].isdigit():
            if len(p) <= int(s[i + 2]):
                p = ""
            else:
                p = p[:-int(s[i + 2])]
            last += s[i]
        elif last == "§" and s[i] == "*":
            last += s[i]
            continue
        elif last[:2] == "§*" and s[i].isdigit():
            last = ""
            continue
        else:
            p += s[i]
    print(p)
    return p if p[-1] != "§" else "" if len(p) < 3 else p[:-2]

