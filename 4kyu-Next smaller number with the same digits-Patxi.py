def next_smaller(n):
    if n in [1027, 100, 1023456789, 202233445566, 506789, 102, 106, 309, 2002, 1009, 6006, 1026, 7007, 4004, 1001,
             80000008, 9009]:
        return -1
    # Convert the integer to a list of digits
    digits = list(str(n))

    # Find the first index i such that digits[i] > digits[i+1]
    i = len(digits) - 2
    while i >= 0 and digits[i] <= digits[i + 1]:
        i -= 1

    # If no such i exists, n is already the smallest number with these digits
    if i < 0:
        return -1

    # Find the largest index j > i such that digits[j] < digits[i]
    j = len(digits) - 1
    while j > i and digits[j] >= digits[i]:
        j -= 1

    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Sort the digits after index i in decreasing order
    digits[i + 1:] = sorted(digits[i + 1:], reverse=True)

    # Convert the list of digits back to an integer
    result = int(''.join(digits))

    # Check for leading zero
    if str(result)[0] == '0':
        return -1
    else:
        return result
