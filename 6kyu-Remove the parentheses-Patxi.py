def remove_parentheses(s):
    import re
    n = 1  # run at least once
    while n:
        s, n = re.subn(r'\([^()]*\)', '', s)  # remove non-nested/flat balanced parts
    return s