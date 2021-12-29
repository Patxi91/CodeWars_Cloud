def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num)-y-1) for y,x in enumerate(num) if x != '0')
