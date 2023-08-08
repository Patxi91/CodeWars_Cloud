def added_char(s1, s2):
    char_count = {}

    for char in s2:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s1:
        char_count[char] -= 1

    for char, count in char_count.items():
        if count > 0:
            return char
