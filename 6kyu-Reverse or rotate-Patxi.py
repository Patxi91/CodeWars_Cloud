def revrot(s, sz):
    if sz <= 0 or not s or sz > len(s):
        return ""

    chunks = [s[i: i + sz] for i in range(0, len(s), sz)]

    if len(chunks[-1]) != sz:
        chunks.pop()
    for c in range(len(chunks)):
        if sum(map(lambda i: int(i) * int(i) * int(i), chunks[c])) % 2 == 0:
            chunks[c] = chunks[c][::-1]
        else:
            chunks[c] = chunks[c][1:] + chunks[c][0:1]

    return ''.join(chunks)
