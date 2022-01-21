def swap(st):
    vowels = 'aeiou'
    return "".join([l.upper() if l.lower() in vowels else l for l in st])
