def longest_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()

    # Create a dictionary to store the frequency of each alphanumeric character
    freq = {}
    for char in s:
        if char.isalnum():
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

    # Initialize variables to store the length of the longest palindrome
    # and a flag to indicate whether there is a character with an odd count
    length = 0
    odd_exists = False

    # Iterate over the frequency of each character
    for count in freq.values():
        # If the count is even, add it to the length
        if count % 2 == 0:
            length += count
        else:
            # If the count is odd, add the largest even number less than it to the length
            length += count - 1
            # Set the flag to True
            odd_exists = True

    # If there is a character with an odd count, add 1 to the length
    if odd_exists:
        length += 1

    return length
