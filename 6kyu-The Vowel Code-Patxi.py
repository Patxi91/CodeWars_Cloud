vowels = {'a': '1',
          'e': '2',
          'i': '3',
          'o': '4',
          'u': '5'}

inv_vowels = {i: v for v, i in vowels.items()}


def encode(st):
    return ''.join(vowels[l] if l in vowels else l for l in st)


def decode(st):
    return ''.join(inv_vowels[l] if l in inv_vowels else l for l in st)
