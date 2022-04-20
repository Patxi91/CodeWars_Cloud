def diamond(n):
    if n % 2 == 0 or n < 1:
        return None

    r = ''

    for i in range(n):
        a = '*' * (i * 2 + 1) if i <= n / 2 else '*' * ((n - i) * 2 - 1)
        r += ' ' * int((n - len(a)) / 2) + a + '\n'

    return r
