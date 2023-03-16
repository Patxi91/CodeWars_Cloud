import string

def keyword_cipher(msg, keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    unused = ''.join([c for c in string.ascii_lowercase if c not in keyword])
    encryption_key = keyword + unused
    translation_table = str.maketrans(string.ascii_lowercase, encryption_key)
    return msg.lower().translate(translation_table)
