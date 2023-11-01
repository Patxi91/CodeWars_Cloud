from decimal import Decimal, getcontext

def fcn(n):
    if n == 0:
        return Decimal(1)
    elif n == 1:
        return Decimal(2)

    getcontext().prec = 1000  # Set precision to handle very large numbers

    u_minus_2 = Decimal(1)
    u_minus_1 = Decimal(2)
    u = 0

    for i in range(2, n + 1):
        u = 6 * u_minus_2 * u_minus_1 / (5 * u_minus_2 - u_minus_1)
        u_minus_2, u_minus_1 = u_minus_1, u

    return u
