def anagram_counter(words):
    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)

    anagram_count = 0
    seen_anagrams = set()

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                pair = tuple(sorted([words[i], words[j]]))
                if pair not in seen_anagrams:
                    seen_anagrams.add(pair)
                    anagram_count += 1

    return anagram_count
