def tribonacci(signature, n):
    if n == 0: return []
    elif n<3: return [signature[x] for x in range(n)]
    res = signature
    for x in range(3,n):
        res.append(sum(res[x-i] for i in range(1,4)))
    return res
print(tribonacci([3, 2, 1], 10))
    
