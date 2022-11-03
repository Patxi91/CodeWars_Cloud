import itertools


def grabscrab(said: str, possible_words :list) -> list:
    return [word for word in possible_words if sorted(said) == sorted(word)]
