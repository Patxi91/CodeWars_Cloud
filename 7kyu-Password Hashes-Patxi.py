import hashlib


def pass_hash(str):
    return hashlib.md5(bytes(str, 'utf-8')).digest().hex()
