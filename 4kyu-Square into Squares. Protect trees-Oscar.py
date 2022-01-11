from math import sqrt
def check(sol,num):
    check = True
    s = 0
    for i in sol:
        s += i**2
        if sol.count(i)>1:
            check = False
    if s != num:
        check = False
    return check
def decompose(n, ex = None):
    sol = []
    num = n**2
    i = num-1
    while i>0 and num >0:
        if sqrt(i)-int(sqrt(i))==0 and i != ex:
            sol = [int(sqrt(i)),*sol]
            num = num-i
            i = num
            print(num)
        else:
            i-=1
        aux = sol
        pos = len(aux)-1
    while not check(sol,n**2) and pos >=0:
        sol = decompose(n,aux[pos])
        pos -=1



    

    return sol





#print(decompose(5))
print(decompose(50))
#print(decompose(11))
#print(decompose(8))
