import random
import string


def generateName():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
