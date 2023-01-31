def sum_of_integers_in_string(s: str) -> int:
    sum = 0
    current_number = 0
    negative = False

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif current_number:
            sum += current_number if not negative else -current_number
            current_number = 0
            negative = False

        if char == '-':
            negative = True

    sum += current_number if not negative else -current_number

    return sum
