def is_esthetic(number, base):
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    digits.reverse()

    for i in range(1, len(digits)):
        if abs(digits[i] - digits[i-1]) != 1:
            return False
    return True

def esthetic(num):
    esthetic_bases = []

    for base in range(2, 11):
        if is_esthetic(num, base):
            esthetic_bases.append(base)

    return esthetic_bases
