def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o') if 'x' or 'o' in s else True
