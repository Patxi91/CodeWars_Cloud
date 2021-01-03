def rectangle_rotation(a, b):
    a = a / 2 ** 0.5
    b = b / 2 ** 0.5
    a = int(a) + 1
    b = int(b) + 1
    sum = 0
    sum = sum + a * b + (b - 1) * (a - 1)
    if sum % 2 == 0:
        sum = sum - 1
    return sum