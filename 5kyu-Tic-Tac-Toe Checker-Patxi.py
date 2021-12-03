def all_equal(lst):
    return not lst or lst.count(lst[0]) == len(lst)


def is_solved(board):

    finished = True

    # Rows
    for i in range(len(board)):
        row = board[i]
        if all_equal(row) and 0 not in row:
            return row[0]  # winner
        else:
            if 0 in row and finished:
                finished = False
    # Columns
    for i in range(len(board)):
        col = [board[ele][i] for ele in range(len(board))]
        if all_equal(col) and 0 not in col:
            return col[0]  # winner
        else:
            if 0 in col and finished:
                finished = False
    # Diagonals
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]
    for d in [d1, d2]:
        if all_equal(d) and 0 not in d:
            return d[0]  # winner
        else:
            if 0 in d and finished:
                finished = False

    return 0 if finished else -1
