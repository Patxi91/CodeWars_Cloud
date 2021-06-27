def validBraces(string):
    temp = []
    for item in string:
        if item in ['[','{','(']:
            temp.insert(0,item)
        if item in [']','}',')']:
            if len(temp) == 0:
                return False
            elif (item == ']' and temp[0] == '[') or (item == '}' and temp[0] == '{') or (item == ')' and temp[0] == '('):
                temp.remove(temp[0])
            else:
                return False
    if len(temp) != 0:
        return False
    else:
        return True
