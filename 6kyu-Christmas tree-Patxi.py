def christmas_tree(height):
    if height == 1:
        return '*'
    result = ''
    for r in range(1, height+1):
        for s in range(r, height):
            result += ' '
        for a in range(1, 2*r):
            result += '*'
        for s in range(r, height):
            result += ' '
        if not r == height:
            result += '\n'
    return result
