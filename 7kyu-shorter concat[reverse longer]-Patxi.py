def shorter_reverse_longer(a: str, b: str) -> str:
    return min([a, b], key=len)+max([a, b], key=len)[::-1]+min([a, b], key=len) if len(a) != len(b) else b+a[::-1]+b
