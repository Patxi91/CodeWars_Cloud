def consecutive(arr, a, b):
    s = ' '.join(str(e) for e in arr)
    return ' '.join(str(e) for e in [a, b]) in s or ' '.join(str(e) for e in [b, a]) in s
