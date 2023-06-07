def anagram_difference(w1, w2):
    w1 = ''.join(w1).lower()
    w2 = ''.join(w2).lower()
    
    # Count the frequency of each letter in both words
    count1 = [0] * 26
    count2 = [0] * 26
    
    for c in w1:
        count1[ord(c) - ord('a')] += 1
    
    for c in w2:
        count2[ord(c) - ord('a')] += 1
    
    # Calculate the total difference in frequencies
    diff = 0
    for i in range(26):
        diff += abs(count1[i] - count2[i])
    
    return diff
