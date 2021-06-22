def high(x):
    word_values = [sum([ord(letter)-96 for letter in word]) for word in x.split()]
    return x.split()[word_values.index(max(word_values))]
