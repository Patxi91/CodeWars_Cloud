def capitalize(s):
    return [''.join([l.upper() if i % 2 == 0 else l for i, l in enumerate(s)]), ''.join([l.upper() if i % 2 != 0 else l for i, l in enumerate(s)])]
