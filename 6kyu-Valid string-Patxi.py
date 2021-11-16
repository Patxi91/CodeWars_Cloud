import difflib


def valid_word_algorithm(seq, word):
    found = True
    while found:
        found = False
        for i in range(len(word)):
            sub = word if i == 0 else word[:-i]
            if sub in seq:
                word = ''.join([li[-1] for li in difflib.ndiff(word, sub) if li[0] != ' '])
                found = True
                break

    if word:
        return False
    else:
        return True


def valid_word(seq, word):
    return valid_word_algorithm(seq, word) or valid_word_algorithm([i[::-1] for i in seq], word[::-1])
