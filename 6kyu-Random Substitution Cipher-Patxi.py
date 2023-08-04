import random


def random_sub():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    substitution_cipher = {original: substituted for original, substituted in zip(alphabet, shuffled_alphabet)}
    return substitution_cipher

