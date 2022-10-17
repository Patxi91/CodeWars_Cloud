d = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def average_string(s):
    try:
        if not s:
            return "n/a"
        a = [d[n] for n in s.split()]
    except:
        return "n/a"
    return list(d.keys())[list(d.values()).index(int(sum(a)//len(a)))]
