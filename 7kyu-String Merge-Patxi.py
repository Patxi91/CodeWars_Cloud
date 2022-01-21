def string_merge(string1, string2, letter):
    i1 = string1.index(letter)
    i2 = string2.index(letter)
    return string1[:i1] + string2[i2:]
