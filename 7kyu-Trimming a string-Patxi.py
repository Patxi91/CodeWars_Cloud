def trim(phrase, size):
    return phrase if size == len(phrase) else phrase[:size-3]+"..." if 3 < size < len(phrase) else phrase[:size]+"..." if size <= 3 else phrase[:size]
