def to_camel_case(text):
    text=text.replace(' ',' ')
    text=text.replace('-',' ')
    text=text.replace('_',' ')
    a=text.split()
    b=''
    for i in range(0,len(a)):
        if i>0:
            a[i]=a[i].capitalize()
        b=b+a[i]
    return b
