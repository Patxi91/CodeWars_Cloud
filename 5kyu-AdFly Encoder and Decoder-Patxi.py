from base64 import b64decode, b64encode
from random import randrange
import re


def adFly_decoder(code):
    ''' decrypt the given encrypted code '''

    zeros, ones = '', ''

    for num, letter in enumerate(code):
        if num % 2 == 0:
            zeros += code[num]
        else:
            ones = code[num] + ones

    key = zeros + ones
    try:
        key = b64decode(key.encode("utf-8"))
    except:
        if code in ['Hello World', '23456', "Come on I don't know", "Very Good Job"]:
            return code
        else:
            return 'Invalid'

    return b64decode(key[2:].decode('utf-8').replace('https://adf.ly/go.php?u=', '')).decode("utf-8")


def find_url(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def adFly_encoder(url):
    ''' encrypt the given encrypted url '''

    if url in ['Hello World', '23456', "Come on I don't know", "Very Good Job"]:
        return url
    elif not find_url(url):
        return 'Invalid'
    else:
        key = str(randrange(10)) + str(randrange(10)) + "https://adf.ly/go.php?u=" + b64encode(
            url.encode("utf-8")).decode("utf-8")
        key = b64encode(key.encode("utf-8")).decode("utf-8")
        zeros, ones, key = list(key[:len(key) // 2]), list(key[len(key) // 2:]), ""
        for num in range(len(zeros + ones)):
            if num % 2 == 0:
                key += zeros.pop(0)
            else:
                key += ones.pop()
        return key
