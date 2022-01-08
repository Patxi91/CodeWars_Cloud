from math import factorial
def listPosition(word):
    sol = 1
    ref = sorted(word)
    checked ={}

    for c in ref:
        #print (ref.count(c))
        if ref.count(c)>1 and c not in checked:
            checked[c] = ref.count(c)
    print(checked)
    
    for i,c in enumerate(word):
        pos = ref.index(c)
        rep=1
        for x in checked:
            if checked[x] >1:
                rep *= factorial(checked[x])

 
        sol = sol + int(factorial(len(ref)-1)/rep)*pos


        if c in checked:
            checked[c] -= 1
        #print(sol)
        ref=ref[:pos]+ref[pos+1:]
        print(ref)


    return sol
  

#print(listPosition('BAAA'))
print(listPosition('BOOKKEEPER'))