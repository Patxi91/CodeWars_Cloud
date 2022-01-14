def decompose(n):
    def _recurse(s, i):
        if s < 0:
            return None
        if s == 0:
            return []
        for j in range(i-1, 0, -1):
            sub = _recurse(s - j**2, j)
            if sub != None:
                return sub + [j]
    return _recurse(n**2, n)

'''
print(decompose(5))
print(decompose(50))
print(decompose(11))
print(decompose(8))
'''
#print(decompose(12))
print(decompose(625))
