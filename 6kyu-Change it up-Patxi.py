def changer(str):
    vowels = "aeiou"
    lowers = "abcdefghijklmnopqrstuvwxyza"
    all = lowers.upper() + lowers
    # Map all alphabetical characters
    nxt_str = "".join(map(lambda x: all[all.index(x) + 1] if x in all else x, str))
    # Map the vowels
    nxt_str = "".join(map(lambda x: x.upper() if x.lower() in vowels else x, nxt_str))
    # Map the consonants
    return "".join(map(lambda x: x.lower() if x.lower() not in vowels else x, nxt_str))
