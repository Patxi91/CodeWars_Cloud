def matrix_multiply(A, B, mod):
    return (
        (A[0] * B[0] + A[1] * B[2]) % mod,
        (A[0] * B[1] + A[1] * B[3]) % mod,
        (A[2] * B[0] + A[3] * B[2]) % mod,
        (A[2] * B[1] + A[3] * B[3]) % mod
    )

def matrix_power(matrix, power, mod):
    if power == 1:
        return matrix
    if power % 2 == 0:
        half_power = matrix_power(matrix, power // 2, mod)
        return matrix_multiply(half_power, half_power, mod)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, power - 1, mod), mod)

def sequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    matrix = (1, 1, 1, 0)
    powered_matrix = matrix_power(matrix, n - 2, 3)

    return powered_matrix[0]
