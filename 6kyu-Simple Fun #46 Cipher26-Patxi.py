def cipher26(message):
    decrypted = []
    sum_mod26 = 0
    for letter in message:
        val = ord(letter) - ord('a')
        decrypted_val = (val - sum_mod26) % 26
        decrypted.append(chr(decrypted_val + ord('a')))
        sum_mod26 = (sum_mod26 + decrypted_val) % 26
    return ''.join(decrypted)
