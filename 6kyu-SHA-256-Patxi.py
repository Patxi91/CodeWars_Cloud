import hashlib

def to_sha256(s):
    sha256 = hashlib.sha256()
    sha256.update(s.encode('utf-8'))
    return sha256.hexdigest()
