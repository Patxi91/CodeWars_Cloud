import codecs


def hex_to_base64(hex: str) -> str:
    return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()[:-1]
