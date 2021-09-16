def group_check(s):
    if s == "":
        return True
    if len(s) % 2 != 0:
        return False
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] in ["[]", "()", "{}"]:
            return group_check(s[:i] + s[i + 2:])
    return False
