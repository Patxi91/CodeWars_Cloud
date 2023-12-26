def beggars(values, n):
    if n == 0:
        return []

    result = [0] * n  # Initialize result list with zeros for each beggar

    for i in range(len(values)):
        result[i % n] += values[i]

    return result
