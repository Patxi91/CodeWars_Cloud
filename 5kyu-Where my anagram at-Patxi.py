def anagrams(word, words):
    sol = []
    for w in words:
        if ''.join(sorted(word)) == ''.join(sorted(w)):
            sol.append(w)
    return sol
