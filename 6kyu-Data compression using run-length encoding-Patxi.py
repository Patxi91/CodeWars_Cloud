def encode(st):
    if not st:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(st)):
        if st[i] == st[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + st[i - 1])
            count = 1

    # Add the count and character for the last group
    encoded.append(str(count) + st[-1])

    return ''.join(encoded)

def decode(st):
    decoded = []
    count = ""

    for char in st:
        if char.isdigit():
            count += char
        else:
            if count:
                decoded.append(char * int(count))
                count = ""
            else:
                decoded.append(char)

    return ''.join(decoded)
