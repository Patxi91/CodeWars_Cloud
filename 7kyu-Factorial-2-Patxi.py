def factorial(n):
    if n<0 or n>12:
        raise ValueError
    else:
        f = 1
        for i in range(1,n+1):
            f = f * i
    return f
