import re

def DNA_strand(dna):
    rep = {"A": "T", "T": "A", "C": "G", "G": "C"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], dna)
    return text
