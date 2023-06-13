def replace_letters(word):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowels = ['a','e','i','o','u']

    result = ""
    for letter in word:
        if letter in vowels:
            index = alphabet.index(letter)
            while True:
                index = (index - 1) % len(alphabet)
                if alphabet[index] in consonants:
                    result += alphabet[index]
                    break
        elif letter in consonants:
            index = alphabet.index(letter)
            while True:
                index = (index + 1) % len(alphabet)
                if alphabet[index] in vowels:
                    result += alphabet[index]
                    break
        else:
            result += letter

    return result
