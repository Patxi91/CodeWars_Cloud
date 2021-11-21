def disemvowel(string_):
    return ''.join([l for l in string_ if l.lower() not in ['a', 'e', 'i', 'o', 'u']])
