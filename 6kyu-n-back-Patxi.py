def count_targets(n, sequence):
    count = 0

    for i in range(n, len(sequence)):
        if sequence[i] == sequence[i - n]:
            count += 1

    return count
