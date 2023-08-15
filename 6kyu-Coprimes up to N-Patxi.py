def coprimes(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = []
    for k in range(1, n):
        if gcd(n, k) == 1:
            result.append(k)

    return result