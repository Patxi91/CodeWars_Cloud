def count_change(money, coins):
    if money == 0:
        return 1
    elif money < 0 or len(coins) == 0:
        return 0
    return count_change(money-coins[0],coins) + count_change(money,coins[1:])
