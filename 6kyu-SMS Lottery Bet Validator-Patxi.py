def validate_bet(game, text):
    numbers = []
    valid_chars = {' ', ','}
    n, m = game

    for char in text.replace(',', ' ').split():
        if char.isdigit():
            numbers.append(int(char))
        elif char not in valid_chars:
            return None

    if len(set(numbers)) != len(numbers) or len(numbers) != n or max(numbers) > m or min(numbers) < 1:
        return None

    sorted_numbers = sorted(numbers)
    return sorted_numbers
