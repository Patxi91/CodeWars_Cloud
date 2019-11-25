def is_square(n):
    root = n**(1/2)#sqrt(n)
    if n < 0:
        return False
    elif int(root + 0.5) ** 2 == n:
        return True
    else:
        return False
