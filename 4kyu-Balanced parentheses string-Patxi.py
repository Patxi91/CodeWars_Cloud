import itertools

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


def balanced_parens1(n, k):
    global arr
    arr = []
    generateParentheses(0, 0, n)
    return arr[-(k+1)] if 0<=k<len(arr) else None


def balanced_parens2(n, k):
    def push_in(s, n1, n2):
        if n1 + n2 == n * 2 and len(res)<=k+1  : res.append(s); return
        if n1 < n and len(res)<=k+1            : push_in(s + '(', n1 + 1, n2)
        if n1 - n2 > 0 and len(res)<=k+1       : push_in(s + ')', n1, n2 + 1)

    res = []; push_in('', 0, 0)
    return res[k] if 0<=k<len(res) else None


def balanced_parens(n, k):
    if k < 0:
        return None
    else:
        gen = list(set([p[:i] + "()" + p[i:] for p in balanced_parens(n - 1) for i in range(0, len(p))])) if n > 1 else ([""], ["()"])[n]
    return next(itertools.islice(gen, k, None))

r = balanced_parens(200, 10e6)








