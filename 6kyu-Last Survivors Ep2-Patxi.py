from string import ascii_lowercase


def next_alpha(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65).lower()


def last_survivors(string):
    while len(set(string)) != len(string):
        for letter in ascii_lowercase:
            instances = string.count(letter)
            string = string.replace(letter, "")
            for i in range(0, instances//2):
                string += next_alpha(letter)
            for i in range(0, instances%2):
                string += letter
    sorted_s = ''.join(sorted(string))
    return sorted_s
