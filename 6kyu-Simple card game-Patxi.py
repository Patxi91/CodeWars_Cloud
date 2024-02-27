def winner(deck_steve, deck_josh):
    # Mapping of card to its value
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Initialize scores
    score_steve = 0
    score_josh = 0

    # Iterate over the decks
    for steve_card, josh_card in zip(deck_steve, deck_josh):
        if card_values[steve_card] > card_values[josh_card]:
            score_steve += 1
        elif card_values[steve_card] < card_values[josh_card]:
            score_josh += 1

    # Determine the winner based on the scores
    if score_steve > score_josh:
        return f"Steve wins {score_steve} to {score_josh}"
    elif score_steve < score_josh:
        return f"Josh wins {score_josh} to {score_steve}"
    else:
        return "Tie"
