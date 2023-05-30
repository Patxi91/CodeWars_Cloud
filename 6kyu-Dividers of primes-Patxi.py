def get_dividers(values, powers):
    dividers = [1]  # Initialize the dividers list with 1, as it's always a divisor
    n = len(values)

    for i in range(n):
        current_dividers = dividers.copy()  # Create a copy of the current dividers

        for j in range(powers[i]):  # Multiply each prime with its powers
            current_dividers = [divider * values[i] for divider in current_dividers]
            dividers.extend(current_dividers)  # Add the new dividers to the main list

    dividers.sort()  # Sort the dividers in ascending order
    return dividers
