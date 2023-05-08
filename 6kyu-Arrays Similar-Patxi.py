def arrays_similar(seq1, seq2):
    if len(seq1) != len(seq2):
        return False

    count1 = {}
    count2 = {}

    for item in seq1:
        count1[item] = count1.get(item, 0) + 1

    for item in seq2:
        count2[item] = count2.get(item, 0) + 1

    return count1 == count2
