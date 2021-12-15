def check(num):
    combinations = ["00","11","88","69","96"]
    i = 0
    j = len(num) - 1
    while i <= j:
        n = num[i] + num[j]
        if not n in combinations:
            return False
        i += 1
        j -= 1
    return True

def solve(a, b):
    cont = 0
    for n in range(a, b):
        if check(str(n)):
            cont += 1
    return cont
