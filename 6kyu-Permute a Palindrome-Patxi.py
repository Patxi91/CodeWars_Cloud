from collections import Counter


def permute_a_palindrome(input):
    return sum(v % 2 for v in Counter(input).values()) <= 1
