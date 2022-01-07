def spiralize(size):
    matrix = list(
        map(lambda x: list(map(lambda y: 1 if (int(size + 1) / 2) % 2 == 1 else 0, range(0, size))), range(0, size)))
    spiral = 1

    for i in range(0, int(size / 2)):
        for j in range(0, size - i * 2):
            matrix[i][j + i] = spiral
            matrix[j + i][i] = spiral
            matrix[size - i - 1][j + i] = spiral
            matrix[j + i][size - i - 1] = spiral

            if size % 4 == 0:
                if i != int(size / 2) - 1:
                    matrix[i + 1][i] = 1 - spiral
            else:
                matrix[i + 1][i] = 1 - spiral
        spiral = 1 - spiral

    return matrix
