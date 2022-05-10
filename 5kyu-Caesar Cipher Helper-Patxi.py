class CaesarCipher(object):

    def __init__(self, shift):
        self.s = shift

    def encode(self, text):
        s = self.s
        text = text.upper()
        result = ""

        # traverse text
        for i in range(len(text)):
            char = text[i]

            if char.isalpha():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += char

        return result

    def decode(self, text):
        s = self.s
        self.s = 26 - self.s
        res = self.encode(text)
        self.s = s
        return res
