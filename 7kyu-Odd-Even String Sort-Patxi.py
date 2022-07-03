def sort_my_string(s):
    even_idx_char = ""
    odd_idx_char = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even_idx_char += s[i]
        else:
            odd_idx_char += s[i]

    return even_idx_char + " " + odd_idx_char
