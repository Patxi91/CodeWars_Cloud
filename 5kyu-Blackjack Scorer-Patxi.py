def score_hand(cards):
    A_c = 0
    sum = 0

    for i in range(len(cards)):
        if cards[i] == 'J' or cards[i] == 'Q' or cards[i] == 'K':
            sum += 10
        elif cards[i] == 'A':
            A_c += 1
        else:
            sum += int(cards[i])

    for i in range(A_c):
        if (sum + (11 * A_c)) > 21:
            sum += 1
            A_c -= 1
        else:
            sum += 11
    print(cards)
    return sum