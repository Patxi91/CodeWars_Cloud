def encrypt_that(word):
    if len(word) > 2:
        return str(ord(word[0]))+word[-1]+word[2:-1]+word[1]
    elif len(word) == 2:
        return str(ord(word[0])) + word[-1]
    elif len(word) == 1:
        return str(ord(word))
    else:
        return ''


def encrypt_this(text):
    return ' '.join([encrypt_that(word) for word in text.split()])
