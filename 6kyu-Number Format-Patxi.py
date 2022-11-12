def number_format(n):
    if n >= 0:
        ns = str(n)[::-1]
        nsc = [ns[i:i + 3] for i in range(0, len(ns), 3)]
        return ','.join(nsc[::-1][::-1])[::-1]
    elif -999 <= n <= 999:
        return str(n)
    else:
        return '-' + number_format(abs(n))
