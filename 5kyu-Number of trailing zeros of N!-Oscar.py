

from typing import Counter


def zeros(n):
    cont = 0
    i = 5

    while n/i >= 1:
        cont += n//i
        i *= 5

    return cont


print(zeros(100))
