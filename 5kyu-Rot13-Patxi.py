def rot13(s):
    if not s:
        return ''
    ss = s.lower()
    d = {i:chr(i+96) for i in range(1, 27)}
    r = [d[list(d.values()).index(l) + 14] if (l.isalpha() and list(d.values()).index(l) < 13) else d[list(d.values()).index(l) + 14 - 26] if (l.isalpha() and list(d.values()).index(l) >= 13) else l for l in ss]
    for l in range(len(s)):
        if s[l].isupper():
            r[l] = r[l].upper()
    return ''.join(r)
