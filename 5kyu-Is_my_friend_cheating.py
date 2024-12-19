'''def remov_nb(n):
    # your code
    def suma_recursiva(n):
        return n * (n + 1) // 2
        
    SUMA = suma_recursiva(n)

    result = []

    for i in range(round(n/2), n, 1):
        SUMA = suma_recursiva(n)-i
        for j in range(round(SUMA/i),0,-1):
            if (round(((SUMA/i)-j)*i)) == j:
                print(i)
                result.append((i,j))
                break

    return result
    '''
def remov_nb(n):
    # Usando la fórmula para la suma de los primeros n números naturales
    SUMA = n * (n + 1) // 2
    result = []

    for i in range(n // 2, n):
        j = (SUMA - i) / (i + 1)
        if j.is_integer() and j <= n:
            result.append((i, int(j)))
print(remov_nb(101))