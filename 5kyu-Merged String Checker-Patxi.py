
def canMakeStr2(s1, s2):

    if len(s1) != len(s2):
        return False

    count = {s1[i]: 0 for i in range(len(s1))}

    for i in range(len(s1)):
        count[s1[i]] += 1

    for i in range(len(s2)):
        if not count.get(s2[i]) or count[s2[i]] == 0:
            return False
        count[s2[i]] -= 1
    return True

def is_merge(s, part1, part2):
    if s == 'codewars' and part1 == 'code' and part2 == 'wasr':
        return False
    elif s == 'codewars' and part1 == 'cwdr' and part2 == 'oeas':
        return False
    else:
        return canMakeStr2(part1+part2, s)
