def clean_string(s):
    p = ""
    for c in s:
        if c == "#":
            p = p[:-1]
        else:
            p += c
    return p
