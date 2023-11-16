def is_keith_number(n):
    digits = [int(digit) for digit in str(n)]
    sequence = digits.copy()

    while sequence[-1] < n:
        next_term = sum(sequence[-len(digits):])
        sequence.append(next_term)

        if next_term == n:
            return len(sequence) - len(digits)

    return False
