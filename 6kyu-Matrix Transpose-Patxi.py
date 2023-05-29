def transpose(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    columns = len(matrix[0])

    # Create a new matrix with swapped rows and columns
    transpose_matrix = [[matrix[j][i] for j in range(rows)] for i in range(columns)]

    return transpose_matrix
