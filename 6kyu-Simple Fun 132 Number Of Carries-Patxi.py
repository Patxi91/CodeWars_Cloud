import math

def number_of_carries(a, b):
    a, b = max(a, b), min(a, b)
    carry = 0
    sol = 0
    while a != 0:
        a_m = a % 10
        b_m = b % 10
        a = math.floor(a/10)
        b = math.floor(b/10)

        if a_m + b_m + carry >= 10:
            carry = 1
            sol += 1
        else:
            carry = 0
    return sol
