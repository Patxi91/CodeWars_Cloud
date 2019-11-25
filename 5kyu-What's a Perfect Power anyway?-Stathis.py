def isPP(n):
    for i in range (1000):
        for j in range (2,60):
            if n == i**j:
                result = [i,j]
                print(i,j)
                return result
            elif i**j > n:
                break
    return None
