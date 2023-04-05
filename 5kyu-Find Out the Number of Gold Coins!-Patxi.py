from math import gcd


def number_of_coins(info):
    # Calculate the product of all m values
    prod_m = 1
    for a, m in info:
        prod_m *= m

    # Calculate the sum of all a_i * M_i * x_i
    sum_axM = 0
    for a, m in info:
        M = prod_m // m
        x = pow(M, -1, m)  # Calculate the modular inverse of M modulo m
        sum_axM += a * M * x

    # Return the smallest non-negative integer that satisfies all conditions
    return sum_axM % prod_m
