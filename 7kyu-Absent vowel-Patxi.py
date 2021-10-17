def absent_vowel(x):
    letters = set(x)
    for i, vowel in enumerate(['a','e','i','o','u']):
        if vowel not in letters:
            return i
