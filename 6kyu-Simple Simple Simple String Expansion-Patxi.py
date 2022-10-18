import re


def string_expansion(s):
    r = ''
    regex = re.compile(r'(\d)?([a-zA-Z]+)+')
    mo = regex.findall(s)

    for i in mo:
        if len(i[1]) > 1:
            l = list(i[1])
            for letter in l:
                if i[0] == '':
                    n = 1
                else:
                    n = i[0]
                letters = letter * int(n)
                r += ''.join(letters)
        else:
            if i[0] == '':
                n = 1
            else:
                n = i[0]
            letters = i[1] * int(n)
            r += ''.join(letters)
    return r
