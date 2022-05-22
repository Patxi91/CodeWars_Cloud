from itertools import takewhile

def take_while(arr, pred_fun):
    return list(takewhile(pred_fun, arr))
