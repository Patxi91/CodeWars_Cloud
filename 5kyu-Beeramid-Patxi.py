def beeramid(bonus, price):
    if bonus < price:
        return 0
    level, beers_level = 1, 1
    while bonus-(beers_level*price) >= 0:
        bonus -= beers_level*price
        level += 1
        beers_level = level**2
    return level-1
