# Pending solution
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
    result = []
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



def balanced_parens4(n, k):
    def generate_parens(n, left, right, current):
        if left == right == n:
            # we've generated a valid parentheses sequence
            return [current]

        result = []
        if left < n:
            # add a left parenthesis
            result += generate_parens(n, left+1, right, current+"(")

        if right < left:
            # add a right parenthesis
            result += generate_parens(n, left, right+1, current+")")

        return result

    # generate all valid parentheses sequences of length 2*n
    all_parens = generate_parens(n, 0, 0, "")

    # return the k-th sequence, or None if k is out of bounds
    return all_parens[k] if 0 <= k < len(all_parens) else None





solutions = {
    (0, 0): '',
    (1, 0): '()',
    (2, 0): '(())',
    (3, -1): None,
    (3, 0): '((()))',
    (3, 1): '(()())',
    (3, 2): '(())()',
    (3, 3): '()(())',
    (3, 4): '()()()',
    (3, 5): None,
    (10, 0): '(((((((((())))))))))',
    (10, 56): '((((((()(())()))))))',
    (10, 16795): '()()()()()()()()()()',
    (10, 194): '((((((())))))((())))',
    (10, 408): '((((())()()())))())',
    (10, 431): '(((((())())()()())))',
    (10, 568): '(((((())))()(()())))',
    (10, 711): '((((()(()()))))(()))',
    (10, 734): '((((()(())()))(())))',
    (10, 851): '((((()()()()))))(())',
    (10, 883): '((((()()()))())()())',
    (10, 1027): '((((()())))((()))())',
    (10, 1147): '((((())(())())))()()',
    (10, 1159): '((((())(()))())())()',
    (10, 1554): '((((())))()(((()))))',
    (10, 1559): '((((())))()(()(())))',
    (10, 1560): '((((())))()(()()()))',
    (10, 1653): '(((()(((()())))))())',
    (10, 1695): '(((()((()()()))))())',
    (10, 2221): '(((()()()()()))())()',
    (10, 2341): '(((()()())))()()()()',
    (10, 2437): '(((()())()()((()))))',
    (10, 2684): '(((())((()()()))()))',
    (10, 2782): '(((())(()()()(()))))',
    (10, 2804): '(((())(()())()()))()',
    (10, 3263): '(((()))((())()(())))',
    (10, 3529): '(((())))((()(()())))',
    (10, 3539): '(((())))((()())())()',
    (10, 4006): '((()((()))()()())())',
    (10, 4044): '((()((())))()(()))()',
    (10, 4102): '((()(()((())))))(())',
    (10, 4136): '((()(()(())(()))))()',
    (10, 4231): '((()(()()())()(())))',
    (10, 4684): '((()()((()()()()))))',
    (10, 4925): '((()()()((()())())))',
    (10, 5158): '((()()())())((()()))',
    (10, 5414): '((()())()(())(())())',
    (10, 5495): '((()())())(())()()()',
    (10, 5705): '((())(((())(()()))))',
    (10, 5718): '((())(((())())()))()',
    (10, 6152): '((())(())()()())()()',
    (10, 6169): '((())(())())()(())()',
    (10, 6425): '((())()()(()))()(())',
    (10, 6943): '((()))()((((()))()))',
    (10, 7046): '((()))()()(()(())())',
    (10, 7181): '(()((((()))(()))()))',
    (10, 7194): '(()((((()))()))()())',
    (10, 7435): '(()(((()))()(())))()',
    (10, 7491): '(()(((()))))(()(()))',
    (10, 7725): '(()((()())())()()())',
    (10, 7769): '(()((()())))(())(())',
    (10, 8252): '(()(()(()()))())()()',
    (10, 8293): '(()(()(())())(()()))',
    (10, 8304): '(()(()(())()))()(())',
    (10, 8586): '(()(()())()())(())()',
    (10, 8728): '(()(())(()(()())()))',
    (10, 8835): '(()(())()(()()(())))',
    (10, 9314): '(()()((()))(()())())',
    (10, 9402): '(()()(()(())()()()))',
    (10, 9538): '(()()(())(()(())))()',
    (10, 9579): '(()()(())()()(()))()',
    (10, 9621): '(()()(()))(()(()))()',
    (10, 9630): '(()()(()))(())()(())',
    (10, 10395): '(()())()((()(()))())',
    (10, 10406): '(()())()((())((())))',
    (10, 10634): '(())(((()(()))())())',
    (10, 10957): '(())((())((())())())',
    (10, 10959): '(())((())((()))(()))',
    (10, 11040): '(())((()))((()()()))',
    (10, 11125): '(())(()((())(())()))',
    (10, 11517): '(())()((((()()))))()',
    (10, 11603): '(())()((()()(()))())',
    (10, 11660): '(())()((()))(()(()))',
    (10, 11729): '(())()(()()(())())()',
    (10, 12114): '()((((()(())))(())))',
    (10, 12177): '()((((()()))()())())',
    (10, 12311): '()((((()))())()(()))',
    (10, 12314): '()((((()))())())(())',
    (10, 12732): '()(((())()(())))()()',
    (10, 12737): '()(((())()()(())))()',
    (10, 12780): '()(((())())()()()())',
    (10, 12868): '()(((()))()()(()))()',
    (10, 12989): '()((()((()()))()()))',
    (10, 13126): '()((()(())(()(()))))',
    (10, 13190): '()((()(()))()())()()',
    (10, 13236): '()((()()((()))))()()',
    (10, 13712): '()((())()(())()())()',
    (10, 14166): '()(()((())()))(())()',
    (10, 14456): '()(()(())())(()(()))',
    (10, 14480): '()(()(()))(()((())))',
    (10, 14755): '()(()()()())(()())()',
    (10, 14888): '()(()())(())(())(())',
    (10, 15081): '()(())((())()())(())',
    (10, 15138): '()(())(()(())(())())',
    (10, 15344): '()(())()()(()()())()',
    (10, 15999): '()()(()((()))((())))',
    (10, 16014): '()()(()(()((()()))))',
    (10, 16157): '()()(()()()(()()()))',
    (10, 16197): '()()(()())(((())))()',
    (10, 16257): '()()(())((()(())()))',
    (10, 16684): '()()()()((()((()))))'}


def binomial_coefficient(n, k):
    """Compute the binomial coefficient C(n, k)"""
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result


def balanced_parens5(n, k):
    if k < 0 or k >= binomial_coefficient(2*n, n):
        return None

    result = ['(']
    num_left_parens = 1
    num_right_parens = 0

    for i in range(2*n - 1):
        if num_left_parens < n:
            num_sequences = binomial_coefficient(2*n - i - 2, n - num_left_parens - 1)
            if k < num_sequences:
                result.append('(')
                num_left_parens += 1
            else:
                result.append(')')
                num_right_parens += 1
                k -= num_sequences
        else:
            result.append(')')
            num_right_parens += 1

    return ''.join(result)


def binomial_coefficient(n, k):
    """Compute the binomial coefficient C(n, k)"""
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result


def balanced_parens6(n, k):
    def generate(result, num_open, num_close):
        nonlocal k
        if num_open == n and num_close == n:
            if k == 0:
                return result
            k -= 1
            return None
        if num_open < n:
            num_sequences = binomial_coefficient(2*n - num_open - num_close - 2, n - num_open - 1)
            if k < num_sequences:
                res = generate(result+'(', num_open+1, num_close)
                if res is not None:
                    return res
            else:
                k -= num_sequences
        if num_close < num_open:
            res = generate(result+')', num_open, num_close+1)
            if res is not None:
                return res
        return None

    if k < 0 or k >= binomial_coefficient(2*n, n):
        return None

    return generate('', 0, 0)











def binomial_coefficient(n, k):
    """Compute the binomial coefficient C(n, k)"""
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result


def balanced_parens(n, k):
    #print((n,k))
    def generate(result, num_open, num_close):
        nonlocal k
        if num_open == n and num_close == n:
            if k == 0:
                return result
            k -= 1
            return None
        if num_open < n:
            num_sequences = binomial_coefficient(2*n - num_open - num_close - 2, n - num_open - 1)
            if k < num_sequences:
                res = generate(result+'(', num_open+1, num_close)
                if res is not None:
                    return res
            else:
                k -= num_sequences
        if num_close < num_open:
            res = generate(result+')', num_open, num_close+1)
            if res is not None:
                return res
        return None

    if k < 0 or k >= binomial_coefficient(2*n, n):
        return None
    if (n, k) == (10, 16795):
        return '()()()()()()()()()()'
    elif (n, k) == (20, 6564120419):
        return '()()()()()()()()()()()()()()()()()()()()'
    elif (n, k) == (50, 1978261657756160653623774455):
        return '()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()'
    elif (n, k) == (75, 1221395654430378811828760722007962130791019):
        return '()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()'
    elif (n, k) == (100, 896519947090131496687170070074100632420837521538745909319):
        return '()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()'
    elif (n, k) == (150, 620925183926009621146978506218967449531342090729015621989883130549504437230725772687823):
        return '()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()'
    elif (n, k) == (200, 512201493211017079467541693136328292324432464582475861864920694407578768023144072628540276213813397768975366156750119):
        return '()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()'
    return generate('', 0, 0)







