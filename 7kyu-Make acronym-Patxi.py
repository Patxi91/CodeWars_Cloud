def to_acronym(inp: str) -> str:
    return ''.join([word[0].upper() for word in inp.split()])
