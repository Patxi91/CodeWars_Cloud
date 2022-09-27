def digits_of(number):
    return [int(i) for i in str(number)]


def validate(card_number: int) -> bool:
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]  # From right
    even_digits = digits[-2::-2]  # From right
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10 == 0
