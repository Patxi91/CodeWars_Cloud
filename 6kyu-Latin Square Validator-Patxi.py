def verify_latin_square(array, m):
    n = len(array)

    # Check if the array is square
    if any(len(row) != n for row in array):
        return "Array not square"

    # Check if the array is of size m
    if n != m:
        return "Array is wrong size"

    # Check for duplicate values in rows
    for row in range(n):
        for value in range(1, n + 1):
            if array[row].count(value) > 1:
                return f"{value} occurs more than once in row {row + 1}"

    # Check for duplicate values in columns
    for col in range(n):
        column_values = [array[row][col] for row in range(n)]
        for value in range(1, n + 1):
            if column_values.count(value) > 1:
                return f"{value} occurs more than once in column {col + 1}"

    # Check for values outside the range 1 to m
    for row in range(n):
        for col in range(n):
            value = array[row][col]
            if not 1 <= value <= m:
                return f"{value} at {row + 1},{col + 1} is not between 1 and {m}"

    # If all checks pass, return a valid message
    return f"Valid latin square of size {m}"
