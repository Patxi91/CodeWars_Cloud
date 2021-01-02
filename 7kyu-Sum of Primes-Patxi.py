def sum_primes(lower, upper):
    upper += 1
    a=list(range(upper))
    return sum(i for i in[[i for a[::i]in[([0]*upper)[::i]]][0]for i in a[2:]if a[i]]if i>=lower)
