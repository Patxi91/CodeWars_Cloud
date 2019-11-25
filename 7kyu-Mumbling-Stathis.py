def accum(s):
    a=list(s)
    l=len(s)
    i=1
    b=''
    for x in a :
        x=(x*i)
        i=i+1
        b=b+x.capitalize()
        if i <= l :
            b=b+'-'
    return b
