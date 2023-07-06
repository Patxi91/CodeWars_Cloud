def conjugate(verb):
    conjugations = {}

    if verb.endswith('ar'):
        suffixes = ['o', 'as', 'a', 'amos', 'áis', 'an']
    elif verb.endswith('er'):
        suffixes = ['o', 'es', 'e', 'emos', 'éis', 'en']
    elif verb.endswith('ir'):
        suffixes = ['o', 'es', 'e', 'imos', 'ís', 'en']
    else:
        return conjugations

    stem = verb[:-2]

    conjugations[verb] = [stem + suffix.replace('á', 'a').replace('é', 'e').replace('í', 'i') for suffix in suffixes]

    return conjugations
