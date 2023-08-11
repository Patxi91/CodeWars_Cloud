def vowel_2_index(string):
    vowels = 'aeiouAEIOU'
    result = []

    for index, char in enumerate(string):
        if char in vowels:
            result.append(str(index + 1))
        else:
            result.append(char)

    return ''.join(result)
