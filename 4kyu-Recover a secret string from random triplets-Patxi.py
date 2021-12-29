from collections import defaultdict

def recoverSecret(subsequences):
    preceding_chars = defaultdict(set)
    for subseq in subsequences:
        for i in range(len(subseq)):
            preceding_chars[subseq[i]].update(subseq[i - 1] if i else '')

    secret = []
    while preceding_chars:
        c = next(k for k, v in preceding_chars.items() if not v)
        del preceding_chars[c]
        for prec in preceding_chars.values():
            if c in prec:
                prec.remove(c)
        secret.append(c)
    return ''.join(secret)
