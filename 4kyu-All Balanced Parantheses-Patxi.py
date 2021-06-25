from itertools import permutations

def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


def balanced_parens1(n):
    return list(set([''.join(p) for p in permutations(n * '()') if matched(p)]))


def generateParentheses(openBr, closeBr, n, s=[]):
    global arr
    if closeBr == n:
        arr.append(''.join(s))
        return

    if closeBr < openBr:
        s.append(')')
        generateParentheses(openBr, closeBr + 1, n, s)
        s.pop()
    if openBr < n:
        s.append('(')
        generateParentheses(openBr + 1, closeBr, n, s)
        s.pop()
    return





def balanced_parens(n):
    global arr
    arr = []
    generateParentheses(0, 0, n)
    return arr
