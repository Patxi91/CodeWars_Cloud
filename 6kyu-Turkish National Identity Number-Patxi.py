def check_valid_tr_number(number):
    # Check if the input is a string or can be converted to one
    number_str = str(number)

    # Check if the input string has exactly 11 digits
    if len(number_str) == 11 and number_str.isdigit():
        digits = [int(digit) for digit in number_str]

        if (
            digits[0] != 0 and
            digits[9] == (sum(digits[i] for i in range(0, 10, 2)) * 7 - sum(digits[i] for i in range(1, 8, 2))) % 10 and
            digits[10] == sum(digits[:10]) % 10
        ):
            return True

    return False
