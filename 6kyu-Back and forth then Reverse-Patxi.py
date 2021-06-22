def arrange(s):
        t = []
        first = 0
        second = len(s)-1
        flag = True
        while first <= second:
            if first == second:
                t.append(s[first])
                break
            else:
                if flag:
                    t.append(s[first])
                    t.append(s[second])
                else:
                    t.append(s[second])
                    t.append(s[first])
                first += 1
                second -= 1
                flag = not flag
        return t
