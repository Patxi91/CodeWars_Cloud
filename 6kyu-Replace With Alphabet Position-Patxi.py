def alphabet_position(text):
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26', "'":''}
    new_text = ''.join(x for x in text if x.isalpha()).lower()
    for i in new_text:
        if i.isalpha() and i in dict:
            new_text = new_text.replace(i, f'{dict[i]} ')
    return " ".join(new_text.split())
