import sys
sys.setrecursionlimit(8000)

factorial_memo = {}  # Dictionary creates cache for known results


def factorial(k):
    if k < 0:
        return None
    if k < 2:
        return 1

    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k - 1)

    return factorial_memo[k]
