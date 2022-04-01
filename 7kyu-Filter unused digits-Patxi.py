def unused_digits(*args):
    return ''.join(sorted({"0","1","2","3","4","5","6","7","8","9"}.difference( set(''.join([str(n) for n in list(locals()['args'])])) )))
