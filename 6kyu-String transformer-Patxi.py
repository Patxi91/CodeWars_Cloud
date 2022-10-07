def string_transformer(s: str) -> str:
    return ' '.join(s.swapcase().split(' ')[::-1])
