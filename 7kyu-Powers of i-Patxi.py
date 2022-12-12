def pofi(n):
    z = 0 + 1j
    real = (z**n).real
    im = (z**n).imag
    if abs(im) < 1e-3 :
        if real < 0:
            return '-1'
        else:
            return '1'
    elif im > 0:
        return 'i'
    else:
        return '-i'
