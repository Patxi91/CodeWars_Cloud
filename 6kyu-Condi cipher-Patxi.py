def encode(message, key, initShift):
    key_alphabet = "".join(sorted(set(key), key=key.index) + sorted(set("abcdefghijklmnopqrstuvwxyz") - set(key)))
    result = ""
    prev_position = initShift

    for char in message:
        if char.isalpha():
            current_position = (key_alphabet.index(char) + prev_position) % 26
            result += key_alphabet[current_position]
            prev_position = key_alphabet.index(char) + 1
        else:
            result += char

    return result

def decode(message, key, initShift):
    key_alphabet = "".join(sorted(set(key), key=key.index) + sorted(set("abcdefghijklmnopqrstuvwxyz") - set(key)))
    result = ""
    prev_position = initShift

    for char in message:
        if char.isalpha():
            current_position = (key_alphabet.index(char) - prev_position) % 26
            result += key_alphabet[current_position]
            prev_position = key_alphabet.index(result[-1]) + 1
        else:
            result += char

    return result
