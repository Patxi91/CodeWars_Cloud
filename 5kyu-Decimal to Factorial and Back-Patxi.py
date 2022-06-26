def dec_2_fact_string(nb):
    print(nb)
    c = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = 1
    n = 2
    while f < nb:
        if n * f < nb:
            f *= n
            n += 1
        else:
            n -= 1
            break
    r = ''
    while n > 0:
        r += c[round(nb // f)]
        nb %= f
        f /= n
        n -= 1
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
