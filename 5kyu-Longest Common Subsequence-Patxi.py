def lcs(s, t):
    if not s or not t:
        return ''
    if s[0] is t[0]:
        return s[0] + lcs(s[1:], t[1:])
    result1 = lcs(s[1:], t)
    result2 = lcs(s, t[1:])
    if len(result1) > len(result2):
        return result1
    else:
        return result2
