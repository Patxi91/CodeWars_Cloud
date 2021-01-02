from collections import Counter

def scramble(s1, s2):
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)
    return not any([counter_s1[char] < counter_s2[char] for char in s2])
