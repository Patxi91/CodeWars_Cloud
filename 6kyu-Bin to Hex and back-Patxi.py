def str_to_int(text, base):
    TABLE = '0123456789abcdefghijklmnopqrstuvwxyz'
    integer = 0
    for character in text:
        if character not in TABLE:
            raise ValueError('found unknown character')
        value = TABLE.index(character)
        if value >= base:
            raise ValueError('found digit outside base')
        integer *= base
        integer += value
    return integer


def dec_to_hex(num):
    if num == 0:
        return '0'
    m, out = '0123456789abcdef', ''
    while num:
        out = m[num % 16] + out
        num //= 16
    return out


def bin_to_hex(binary_string):
    return dec_to_hex(str_to_int(binary_string, 2))


#

def hex_to_dec(s):
    _hexer = dict(map(reversed, enumerate("0123456789ABCDEF")))
    return sum([_hexer[var] * 16 ** i for i, var in enumerate(reversed(s.upper()))])


def dec_to_bin(number):
    if number == 0:
        return '0'
    elif number < 0:
        return 'Not positive'
    i = 0
    result = ''
    while number >> i:
        result = ('1' if number >> i & 1 else '0') + result
        i += 1
    return result


def hex_to_bin(hex_string):
    return dec_to_bin(hex_to_dec(hex_string))
