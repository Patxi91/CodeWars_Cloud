def locker_run(m):
    if m == 0 or m == 1:
        return [i for i, x in enumerate([True],1) if x]
    doors = [False] * m  # Closed
    for i in range(1, m+1):
        root = i ** 0.5
        if root == int(root):
            doors[i-1] = True
        else:
            doors[i-1] = False
    sol.append(sum(doors))
    return [i for i, x in enumerate(doors,1) if x]
