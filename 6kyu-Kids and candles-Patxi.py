import math

def candies_to_buy(amount_of_kids_invited):
    candies = 1
    for i in range(2, amount_of_kids_invited+1):
        candies = candies*i//math.gcd(candies, i)
    return candies
