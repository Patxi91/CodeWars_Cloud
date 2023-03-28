def longest_repetition(chars):
    if not chars:
        return ('', 0)

    prev_char = chars[0]
    max_char = prev_char
    max_count = 1
    count = 1

    for char in chars[1:]:
        if char == prev_char:
            count += 1
        else:
            if count > max_count:
                max_char = prev_char
                max_count = count
            prev_char = char
            count = 1

    if count > max_count:
        max_char = prev_char
        max_count = count

    return (max_char, max_count)
