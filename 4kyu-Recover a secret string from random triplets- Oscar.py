
def recoverSecret(triplets):
    sol = {}
    checked = []
    for t in triplets:
        for c in t:
            if c not in sol:
                sol[c] = 0
        sol = checkTriplet(t,sol)
        checked.append(t)
        for l in checked:
            sol = checkTriplet(l,sol)
    sol = sorted(sol.items(),key=lambda x: x[1])
    return ''.join([x[0] for x in sol])



    return sol

def checkTriplet(t,sol):
    if sol[t[0]] >= sol[t[1]]:
        sol[t[1]] = sol[t[0]]+1
    if sol[t[1]] >= sol[t[2]]:
        sol[t[2]] = sol[t[1]]+1
    return sol






triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
print(recoverSecret(triplets))



    


