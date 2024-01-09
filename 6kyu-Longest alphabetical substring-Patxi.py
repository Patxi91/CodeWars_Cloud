def longest(st):
    if not st:
        return ""

    current_substring = st[0]
    longest_substring = st[0]

    for i in range(1, len(st)):
        if ord(st[i]) >= ord(st[i - 1]):
            current_substring += st[i]
        else:
            current_substring = st[i]

        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring

    return longest_substring
