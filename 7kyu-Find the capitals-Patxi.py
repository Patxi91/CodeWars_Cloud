def capitals(word):
    return [idx for idx in range(len(word)) if word[idx].isupper()]
