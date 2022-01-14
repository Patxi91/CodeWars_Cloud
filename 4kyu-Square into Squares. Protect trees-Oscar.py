def decompose(n):
    total = 0
    answer = [n]
    while len(answer):
        print(answer)
        temp = answer.pop()
        total += temp ** 2
        for i in range(temp - 1, 0, -1):
            if total - (i ** 2) >= 0:
                total -= i ** 2
                answer.append(i)
                if total == 0:
                    return sorted(answer)
    return None
'''
print(decompose(5))
print(decompose(50))
print(decompose(11))
print(decompose(8))
'''
#print(decompose(12))
print(decompose(625))
