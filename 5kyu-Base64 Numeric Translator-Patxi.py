def base64_to_base10(str):
    return sum('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(j)*64**i for i,j in enumerate(str[::-1]))
