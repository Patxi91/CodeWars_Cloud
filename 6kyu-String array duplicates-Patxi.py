def dup(arry):
    # Initialize an empty list to store the modified strings
    modified_strings = []

    # Iterate through each string in the array
    for string in arry:
        # Initialize an empty string to store the modified string
        modified_string = ""

        # Initialize a previous character variable
        prev_char = None

        # Iterate through each character in the string
        for char in string:
            # If the current character is not the same as the previous character or the previous character is None, append it to the modified string
            if char != prev_char or prev_char is None:
                modified_string += char

            # Set the current character as the previous character
            prev_char = char

        # Append the modified string to the modified_strings list
        modified_strings.append(modified_string)

    return modified_strings
