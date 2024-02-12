def dec_2_fact_string(nb):
    c = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = [1]
    n = 2
    while f[-1] < nb:
        f.append(f[-1] * n)
        n += 1
    r = ''
    for i in range(len(f)-2, -1, -1):
        r += c[nb // f[i]]
        nb %= f[i]
    return r + '0'


def fact_string_2_dec(string):
    c = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = string[::-1]
    s = 0
    f = 1
    for i in range(1, len(string)):
        f *= i
        s += f * c.index(string[i])
    return s
