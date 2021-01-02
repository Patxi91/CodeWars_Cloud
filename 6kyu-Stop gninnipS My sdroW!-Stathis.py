def spin_words(sentence):
    words = sentence.split(' ')
    reversed_words = []
    for word in words:
        if len(word) >= 5:
            reversed_words.append(word[::-1])
        else:
            reversed_words.append(word)
            
    return ' '.join(reversed_words)
