def alphabet_position(text):
    return " ".join([str(ord(x)-96) for x in text if 96<ord(x)<123])




print(alphabet_position("The sunset sets at twelve o' clock."))