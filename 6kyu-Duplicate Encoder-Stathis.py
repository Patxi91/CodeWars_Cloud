def duplicate_encode(word):
    return ''.join([')' if word.lower().count(char) > 1 else '(' for char in word.lower()])
