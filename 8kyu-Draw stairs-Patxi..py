def draw_stairs(n):
    s = ''
    for x in range(n-1):
        s += (' '*x +'I\n')
    s += (' '*(n-1) +'I')
    return s
