def toJadenCase(string):
    return ' '.join([word.capitalize() for word in string.split(' ')])
