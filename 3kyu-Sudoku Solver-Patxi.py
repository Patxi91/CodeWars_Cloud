def check(puzzle, i, row, col):
    rows = puzzle[int(row)]
    column = [puzzle[r][col] for r in range(0,9,1)]
    if i in rows:
        return False
    if i in column:
        return False
    SquareRow = (row // 3)*3
    squareColumn = (col // 3)*3
    Square = [puzzle[y][z] for y in range(SquareRow, SquareRow+3) for z in range(squareColumn, squareColumn+3)]
    if i in Square:
        return False
    return True


def find(puzzle):
    for i in range(0,9,1):
        for j in range(0,9,1):
            if puzzle[i][j]==0:
                return i,j
    return None


def solve(board):
    finds = find(board)
    if not finds:
        return True
    else:
        row, col = finds

    for i in range(1,10):
        if check(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def sudoku(puzzle):
    solve(puzzle)
    return puzzle
