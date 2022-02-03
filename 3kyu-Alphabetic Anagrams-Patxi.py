from math import factorial


def combos(word):
    combo = factorial(len(word))
    for i in set(word):
        combo = combo//factorial(word.count(i))
    return combo


def listPosition(word):
    if len(word) == 1:
        return 1
    check = "".join(sorted(word, key= lambda x: x[0]))
    s = 0
    for i in range(len(check)):
        temp = check.replace("_","")
        index = check.index(word[i])
        check = check[:index]+"_"+check[index+1:]
        s += (temp.index(word[i])*combos(temp))//len(temp)
    return s + 1
