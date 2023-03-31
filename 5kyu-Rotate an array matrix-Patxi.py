def rotate(matrix, direction):
    if direction == "clockwise":
        # Transpose the matrix
        matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        # Reverse each row of the transposed matrix
        matrix = [row[::-1] for row in matrix]
    elif direction == "counter-clockwise":
        # Reverse each row of the matrix
        matrix = [row[::-1] for row in matrix]
        # Transpose the reversed matrix
        matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return matrix
