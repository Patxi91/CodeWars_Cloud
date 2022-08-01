from functools import reduce

def calculator(txt):
    txt = txt.replace(" ", "")
    if '+' in txt:
        return reduce(lambda x, y:x+y, [len(s) for s in txt.split("+")]) * '.'
    if '-' in txt:
        return reduce(lambda x, y:x-y, [len(s) for s in txt.split("-")]) * '.'
    if '*' in txt:
        return reduce(lambda x, y:x*y, [len(s) for s in txt.split("*")]) * '.'
    if '//' in txt:
        return reduce(lambda x, y:x//y, [len(s) for s in txt.split("//")]) * '.'