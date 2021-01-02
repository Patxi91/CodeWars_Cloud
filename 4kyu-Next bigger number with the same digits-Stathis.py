def next_bigger(n):
    n= str(n)
    reverse= ''.join(sorted(n))
    if n==reverse[::-1]:
        return -1
    
    n = int(n)
    for num in range (n+1,10*n):
        num = str(num)
        numl = list(num)
        n = str(n)
        found= []
        for j in n :
            if j in numl:
                found.append(True)
                numl.remove(j)
            else:
                found.append(False)
        if all(found) and len(numl)==0:           
            return int(num)
