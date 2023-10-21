def faro_cycles(deck_size):
    original_order = list(range(deck_size))  # Create a list representing the original order
    current_order = list(range(deck_size))  # Initialize the current order as the original order
    shuffles = 0  # Initialize the shuffle count

    while True:
        # Perform a faro shuffle
        new_order = []
        for i in range(deck_size // 2):
            new_order.append(current_order[i])
            new_order.append(current_order[i + deck_size // 2])

        current_order = new_order  # Update the current order
        shuffles += 1  # Increment the shuffle count

        if current_order == original_order:
            return shuffles  # Deck is restored, return the number of shuffles
