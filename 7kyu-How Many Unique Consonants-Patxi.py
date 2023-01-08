def count_consonants(text):
    return len([l for l in ''.join(set(text.lower())) if l.lower() in 'qzwsxdcrfvtgbyhnjmklp'])
