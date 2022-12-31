def get_the_vowels(word):
    vowels = 'aeiou'
    vowels_idx = 0
    r = 0
    for i in range(len(word)):
        if word[i] == vowels[vowels_idx]:
            r += 1
            if vowels_idx == 4:
                vowels_idx = 0
            else:
                vowels_idx += 1
    return r
