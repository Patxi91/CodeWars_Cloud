def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels:
            right -= 1
        else:
            left += 1

    return ''.join(s)
