'''
it works after few attems I don`t know why it was not working in 1 of the test every time.
I think this program works
'''


from math import factorial
def listPosition(word):
    sol = 1
    ref = sorted(word)
    checked ={}

    for c in ref:
        if ref.count(c)>1 and c not in checked:
            checked[c] = ref.count(c)
    
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


    return sol
  

#print(listPosition('BAAA'))
print(listPosition('MNSVJKPKBQUHLHWDSXPONWVWR'))
#13555280727373304201470

from collections import Counter

def istPosition(word):
    l, r, s = len(word), 1, 1
    c = Counter()

    for i in range(l):
        x = word[(l - 1) - i]
        c[x] += 1
        for y in c:
            if (y < x):
                r += s * c[y] // c[x]
        s = s * (i + 1) // c[x]
    return r

print(istPosition('MNSVJKPKBQUHLHWDSXPONWVWR'))