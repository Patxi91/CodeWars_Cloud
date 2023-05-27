def create_euler_square(n):
    latin_square1 = []
    latin_square2 = []

    for i in range(n):
        row1 = []
        row2 = []
        for j in range(n):
            row1.append((j + i) % n + 1)
            row2.append((j + 2 * i) % n + 1)
        latin_square1.append(row1)
        latin_square2.append(row2)

    return latin_square1, latin_square2
