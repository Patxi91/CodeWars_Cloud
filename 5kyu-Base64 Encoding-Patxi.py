import base64 as b64


def to_base_64(string):
    return b64.b64encode(str.encode(string)).decode().replace("=", "")


def from_base_64(string):
    string += "=" * ((4 - len(string) % 4) % 4)
    return b64.b64decode(string).decode()
