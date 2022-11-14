def vowel_one(s):
    return "".join(["1" if l.lower() in ('a', 'e', 'i', 'o', 'u') else "0" for l in s])
