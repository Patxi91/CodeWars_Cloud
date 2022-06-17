def decrypt(encrypted_text, n):
    for x in range(n):
        de_one = ""
        de_two = ""
        mid = int(len(encrypted_text) / 2)  # mid index
        de_one += encrypted_text[0:mid]  # break in 2 strings
        de_two += encrypted_text[mid:]
        s = ""

        for i in range(0, mid):
            s += de_two[i] + de_one[i]  # alternating even and odd indices

        if len(encrypted_text) % 2 != 0:
            s += de_two[mid]  # if length is odd , add the last index of de_two
        encrypted_text = s
    return encrypted_text


def encrypt(text, n):
    for x in range(n):

        even_chars = []
        odd_chars = []

        for i in range(len(text)):
            if i % 2 == 0:
                even_chars.append(text[i])
            else:
                odd_chars.append(text[i])
        text = ''.join(odd_chars) + ''.join(even_chars)
    return text
