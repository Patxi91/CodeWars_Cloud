import re


def to_underscore(string):
    return '_'.join([word.lower() for word in re.findall('[A-Z][^A-Z]*', string)]) if not str(string).isdigit() else str(string)
