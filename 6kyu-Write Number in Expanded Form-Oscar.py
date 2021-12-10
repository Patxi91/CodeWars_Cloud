'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
'''

def expanded_form(num):
    num = str(num)
    index = 0
    sol = ""
    first = True
    for i in reversed(num):
        if i !='0' and not first:
            sol =str(int(i)*10**index)+' + '+sol
        elif i !='0' and first:
            first = False
            sol = str(int(i)*10**index)
        index +=1
    return sol

print(expanded_form(70304))
            