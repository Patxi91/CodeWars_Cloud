def ds_multof_pfs(nMin, nMax):
    def prime_factors_sum(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return sum(factors)

    def divisors_sum(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        divisors.append(n)
        return sum(divisors)

    result = [num for num in range(nMin, nMax + 1) if divisors_sum(num) % prime_factors_sum(num) == 0]
    return result
