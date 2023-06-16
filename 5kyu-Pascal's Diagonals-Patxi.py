def generate_diagonal(n, l):
    if l == 0:
        return []

    diagonal = [1]  # The first number in each diagonal is 1

    for i in range(1, l):
        next_number = diagonal[i - 1] * (n + i) // i
        diagonal.append(next_number)

    return diagonal
