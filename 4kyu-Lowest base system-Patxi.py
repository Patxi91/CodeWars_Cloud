import math


def check_digits1(num, b):
    while num % b == 1:
        if num == 1:
            return True
        num //= b
    return False


def check_digits2(num, b):
    return math.log(num * (b - 1) + 1, b).is_integer()


def get_min_base(num):
    print(num)
    if num < 1250025000500010:
        for i in range(2, int(num**0.5) + 2):
            if check_digits1(num, i):
                return i
    else:
        for i in range((int(num**0.5) + 2)//2, int(num**0.5) + 2):
            if check_digits2(num, i):
                return i
        for i in range(2, (int(num**0.5) + 2)//2 +1):
            if check_digits1(num, i):
                return i
    return num - 1
