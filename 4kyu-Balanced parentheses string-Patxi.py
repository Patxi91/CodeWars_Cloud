def calculate_parentheses(num_open, num_close, parentheses_table):
    if num_open == 0 and num_close == 0:
        parentheses_table[num_open][num_close] = 1
        return 1
    if parentheses_table[num_open][num_close] > 0:
        return parentheses_table[num_open][num_close]

    if num_open > 0:
        parentheses_table[num_open][num_close] += calculate_parentheses(num_open - 1, num_close + 1, parentheses_table)
    if num_close > 0:
        parentheses_table[num_open][num_close] += calculate_parentheses(num_open, num_close - 1, parentheses_table)

    return parentheses_table[num_open][num_close]


def construct_sequence(num_open, num_close, sequence_rank, parentheses_table):
    if num_open == 0 and num_close == 0:
        return ''

    if num_open > 0:
        if parentheses_table[num_open - 1][num_close + 1] >= sequence_rank:
            return '(' + construct_sequence(num_open - 1, num_close + 1, sequence_rank, parentheses_table)
        else:
            sequence_rank -= parentheses_table[num_open - 1][num_close + 1]
    if num_close > 0:
        return ')' + construct_sequence(num_open, num_close - 1, sequence_rank, parentheses_table)

    return ''


def balanced_parens(n, k):
    parentheses_table = [[0 for _ in range(201)] for _ in range(201)]
    k += 1
    if k < 1 or k > calculate_parentheses(n, 0, parentheses_table):
        return None
    return construct_sequence(n, 0, k, parentheses_table)
