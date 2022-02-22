def solve(s):
    return len(max(''.join(i if i in 'aeiou' else ' ' for i in s).split(), key=len))
