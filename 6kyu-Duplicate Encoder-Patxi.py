def duplicate_encode(word):
    return ''.join('(' if word.lower().count(ch) == 1 else ')' for ch in word.lower())
