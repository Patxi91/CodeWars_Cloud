def validBraces(string):
    len_before = len(string)
    len_after = 0
    types = ['()', '{}', '[]']
    while len_before != len_after:
        len_before = len(string)
        for type in types:
            string = string.replace(type, '')
            len_after = len(string)

    return len(string) == 0
