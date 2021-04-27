import hashlib


def crack(hash):
    for code in range(100000):
        code_s = '{0:05}'.format(code)
        if hashlib.md5(bytes(code_s, 'utf-8')).hexdigest() == hash:
            return code_s
