def bingo(array):
    return 'WIN' if all([c in ''.join([chr(ord('@')+x) for x in array]).upper() for c in 'BINGO']) else 'LOSE'
