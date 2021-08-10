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


def binomialCoeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)
    return int(res)


def catalan(n):
    c = binomialCoeff(2 * n, n)
    return int(c / (n + 1))


def findWays(n):
    if n & 1:
        return 0
    return catalan(int(n / 2))


def balanced_parens3(n, k):
    stack = [('', n, 0)]
    #result = []
    count = 0
    k_my = (findWays(2*n)-1)-k

    # Loop until we run out of items in the stack
    while stack:
        current, left, right = stack.pop()

        # if no '(' or ')' left to add, add current to the result
        if left == 0 and right == 0:
            #result.append(current)
            count += 1
            if k_my == count-1:#len(result)-1:
                return current

        # if we can, add a '(' and return to the stack
        if left > 0:
            stack.append((current + '(', left - 1, right + 1))

        # if we can, add a ')' and return to the stack
        if right > 0:
            stack.append((current + ')', left, right - 1))

    return sorted(result)[k] if 0 <= k < len(result) else None


r = balanced_parens3(66, 344)  # "()()()"








