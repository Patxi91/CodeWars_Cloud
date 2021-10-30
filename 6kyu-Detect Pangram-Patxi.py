import string


def is_pangram(s):
    v = []
    for character in s:
        if character.isalpha():
            v.append(character)
    v = ''.join(v)

    alphabet = set(string.ascii_lowercase)

    return set(v.lower()) >= alphabet
