def mispelled(word1: str, word2: str) -> bool:
    if word1 == word2:
        return True

    if abs(len(word1) - len(word2)) > 1:
        return False

    if len(word1) > len(word2):
        word1, word2 = word2, word1

    i = j = 0
    count_diff = 0

    while i < len(word1) and j < len(word2):
        if word1[i] != word2[j]:
            count_diff += 1
            if count_diff > 1:
                return False
            if len(word1) == len(word2):
                i += 1
        else:
            i += 1
        j += 1

    if count_diff == 1 or (count_diff == 0 and len(word1) != len(word2)):
        return True

    return False
