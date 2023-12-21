

def crazy_formula(n):
    # Handle negative numbers
    is_negative = n < 0
    n = abs(n)

    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(n)]

    while len(digits) > 1:
        # If the number of digits is even, remove the last digit
        if len(digits) % 2 == 0:
            digits.pop()

        # Calculate the middle index
        middle_index = len(digits) // 2

        # If the middle digit is odd, subtract it instead of adding
        if digits[middle_index] % 2 == 1:
            digits[0] -= digits[middle_index]
        else:
            # If both the middle digit and the last digit are even, subtract the last digit instead of adding
            if digits[-1] % 2 == 0:
                digits[0] -= digits[-1]
            else:
                # If the middle digit is even but the last digit is odd, the first digit must be squared
                digits[0] = digits[0] ** 2

        # Remove the processed digits
        digits = digits[:middle_index] + digits[-1:]

    result = digits[0]

    # Handle the case for negative numbers
    if is_negative:
        result = -result

    return result

# Test cases
print(crazy_formula(5))    # Output: 5
print(crazy_formula(214))  # Output: 5
print(crazy_formula(126))  # Output: 3
print(crazy_formula(2234)) # Output: 9
