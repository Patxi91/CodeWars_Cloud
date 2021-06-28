from collections import Counter
import re

def top_3_words(text):
    words = re.findall("[\s]?([']?[A-Za-z]+'?[A-Za-z']*)[\s,:]?", text)
    c = Counter()
    for x in words:
        c[x.lower()] += 1
    return [x[0] for x in c.most_common(3)]
