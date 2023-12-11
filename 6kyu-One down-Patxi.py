def one_down(txt):
    if not isinstance(txt, str):
        return "Input is not a string"

    result = []
    for char in txt:
        if char.isalpha():
            # Shift the letter one position to the left in the alphabet
            if char.isupper():
                result.append(chr((ord(char) - 65 - 1) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 - 1) % 26 + 97))
        else:
            result.append(char)

    return ''.join(result)
