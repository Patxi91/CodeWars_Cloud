def first_non_repeating_letter(string):
    if not string:
        return ''
    for n in range(len(string)):
        if string.upper().count(string[n].upper()) == 1:
            return string[n]
    return ''
