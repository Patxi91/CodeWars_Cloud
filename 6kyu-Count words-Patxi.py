import re


def word_count(s):
    r = ['a', 'the', 'on', 'at', 'upon', 'of', 'in', 'as']
    sol = s

    alphanumeric = [character if character.isalnum() else " " for character in sol]
    sol = "".join(alphanumeric)
    sol = re.sub(r'[0-9]', ' ', sol)
    sol = sol.split()
    count = 0
    sol = [x.lower() for x in sol]
    while count != len(sol):
        count = len(sol)
        [sol.remove(ele) for ele in r if ele in sol]
    return len(sol)
