def reverse_number(n, b):
    if b == 1:
        return n

    reversed_num = 0
    power = 0

    while n > 0:
        remainder = n % b
        reversed_num = reversed_num * b + remainder
        n //= b
        power += 1

    return reversed_num
