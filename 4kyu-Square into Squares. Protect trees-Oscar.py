from math import sqrt
def check(sol,num):
    s = 0
    if s == None:
        return False
    for i in sol:
        s += i**2
        if sol.count(i)>1:
            return 'repeated'
    if s != num:
        return False
    
    return True

def recheck(n,sol):
    for j,ex in enumerate(sol):
        while ex >0:
            sol1 = sol[j+1:]
            num = sum([x**2 for x in sol[:j+1]])
            i = ex-1
            while i>0 and num>0:
                if num - i**2 > -1:
                    if i in sol1:
                        num =0
                    else:
                        num -= i**2
                        #print(sol1)
                        sol1 = sorted([i,*sol1])
                        i = int(sqrt(num))
                        
                else:        
                    i -= 1
            ex-=1
            print(sol1)
            if check(sol1,n**2)==True:
                return sol1
    return None



def decompose(n):
    ex = None
    sol = []
    num = n**2
    i = n-1
    while i>0 and num >0:
        if num- i**2 > -1:
            num -= i**2
            sol = sorted([i,*sol])
            i = int(sqrt(num))
        else:        
            i -= 1
    if check(sol,n**2) =='repeated':
        sol = recheck(n,sol)
    elif check(sol,n**2)==False:
        sol = None
   
    return sol




'''
print(decompose(5))
print(decompose(50))
print(decompose(11))
print(decompose(8))
print(decompose(12))
'''
print(decompose(625))
