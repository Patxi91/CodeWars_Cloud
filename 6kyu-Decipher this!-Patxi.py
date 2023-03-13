def decipher_this(s):
    # split the string into words
    words = s.split()

    # loop through each word and decipher it
    deciphered_words = []
    for word in words:
        # get the ascii code of the first character
        first_char = chr(int(''.join(filter(str.isdigit, word))))

        # get the remaining characters and perform the letter switching
        remaining_chars = list(word[len(str(ord(first_char))):])
        if len(remaining_chars) > 1:
            remaining_chars[0], remaining_chars[-1] = remaining_chars[-1], remaining_chars[0]

        # concatenate the deciphered word
        deciphered_words.append(first_char + ''.join(remaining_chars))

    # return the deciphered sentence
    return ' '.join(deciphered_words)
