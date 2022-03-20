def filter_long_words(sentence, n):
    l = sentence.split(' ')
    return [w for w in l if len(w)>n]
