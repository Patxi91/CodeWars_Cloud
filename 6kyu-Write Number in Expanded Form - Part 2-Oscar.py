'''
Write Number in Expanded Form - Part 2
This is version 2 of my 'Write Number in Exanded Form' Kata.

You will be given a number and you will need to return it as a string in expanded form :

expanded form illustration

For example:

expanded_form(807.304) # Should return '800 + 7 + 3/10 + 4/1000'
expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
expanded_form(0.04) # Should return '4/100'
'''

def expanded_form(num):
    num = list(str(num))
    ind = num.index('.')
    res = []
    for i in range(len(num)):
        if i<ind and num[i] != '0': 
            res.append(str(int(num[i])*10**(ind-i-1)))
        elif i>ind and num[i] !='0':
            res.append(num[i]+'/'+str(10**(i-ind)))

    return ' + '.join(res)

print(expanded_form(1.24))