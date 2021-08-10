import re


def alphanumeric(password):
    return len(password) > 0 and not " " in password and not "_" in password if not re.search(r"[^\.a-zA-Z0-9]",password) else False
