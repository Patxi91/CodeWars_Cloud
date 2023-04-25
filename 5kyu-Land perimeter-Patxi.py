def land_perimeter(arr):
    rows = len(arr)
    cols = len(arr[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 'X':
                if i == 0 or arr[i-1][j] == 'O':  # top
                    perimeter += 1
                if i == rows-1 or arr[i+1][j] == 'O':  # bottom
                    perimeter += 1
                if j == 0 or arr[i][j-1] == 'O':  # left
                    perimeter += 1
                if j == cols-1 or arr[i][j+1] == 'O':  # right
                    perimeter += 1
    return f"Total land perimeter: {perimeter}"
