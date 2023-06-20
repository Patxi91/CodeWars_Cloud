def square_digits_sequence(n):
    sequence = [n]  # Initialize the sequence with the first element
    seen = set([n])  # Keep track of the elements that have already appeared

    while True:
        # Calculate the next element by summing the squared digits of the previous element
        next_element = sum(int(digit) ** 2 for digit in str(sequence[-1]))

        # If the next element is already in the sequence, return the length of the sequence
        if next_element in seen:
            return len(sequence) + 1  # Add 1 to account for the repeated element

        # Add the next element to the sequence and mark it as seen
        sequence.append(next_element)
        seen.add(next_element)
