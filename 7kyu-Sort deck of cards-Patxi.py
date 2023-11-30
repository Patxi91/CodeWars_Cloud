def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank."""
    rank_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    return sorted(cards, key=lambda card: rank_order.index(card))
