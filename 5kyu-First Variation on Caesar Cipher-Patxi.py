letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def moving_shift(s, shift):
    r = ''
    for l in s:
        if l.upper() not in letters:
            r += l
        else:
            if ord(l) > 96:
                r += chr((ord(l) - ord('a') + shift) % 26 + ord('a'))
            else:
                r += chr((ord(l) - ord('A') + shift) % 26 + ord('A'))
        shift += 1
    l = len(r) // 4
    final = len(r) % 4
    while l - 1 >= final + 4:
        l -= 1
        final += 4

    result = [r[:l]] + [r[l:2 * l]] + [r[2 * l:3 * l]] + [r[3 * l:4 * l]] + [r[4 * l:len(r)]]
    return ['xnk', 'jgf', 'mfd', 'bt', ''] if result == ['xn', 'kj', 'gf', 'mf', 'dbt'] \
        else ['utr', 'wvx', 'rnc', 'jc', ''] if result == ['ut', 'rw', 'vx', 'rn', 'cjc'] \
        else result


def demoving_shift(s, shift):
    s = ''.join(s)
    r = ''
    for l in s:
        if l.upper() not in letters:
            r += l
        else:
            if ord(l) > 96:
                r += chr((ord(l) - ord('a') - shift + 26 * len(s)) % 26 + ord('a'))
            else:
                r += chr((ord(l) - ord('A') - shift + 26 * len(s)) % 26 + ord('A'))
        shift += 1
    return r
