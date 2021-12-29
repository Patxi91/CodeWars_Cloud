def number_of_pairs(gloves):
    pairs = 0
    if gloves:
        for color in list(set(gloves)):
            sub_pair = int(gloves.count(color)/2)
            pairs += sub_pair
    return pairs
