
'''import itertools

def next_bigger(n):
    num = str(n)
    permutaciones = []
    for p in  itertools.permutations(num):
        if (int(''.join(p)) > n):
            permutaciones.append(int(''.join(p)))
            permutaciones = sorted(permutaciones)
    print(permutaciones)

    if permutaciones != []:
        return permutaciones[0]
    
    return -1'''
def next_bigger(n):
    # Convertir el número a una lista de dígitos
    digits = list(str(n))
    
    # Encontrar el primer dígito que se puede intercambiar para formar un número mayor
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1  # Si no se encuentra tal dígito, devolver -1
    
    # Encontrar el dígito más pequeño a la derecha de digits[i] que sea mayor que digits[i]
    for j in range(len(digits) - 1, i, -1):
        if digits[j] > digits[i]:
            break
    
    # Intercambiar los dígitos
    digits[i], digits[j] = digits[j], digits[i]
    
    # Ordenar los dígitos a la derecha de i en orden ascendente
    digits = digits[:i + 1] + sorted(digits[i + 1:])
    
    # Convertir la lista de dígitos de nuevo a un número entero
    return int(''.join(digits))
        


print(next_bigger(4459887665440))
        
        