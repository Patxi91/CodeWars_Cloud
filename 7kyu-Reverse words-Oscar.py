'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    text = list(text)
    aux = []
    pos = 0
    for i in range(len(text)):
        if text[i] == ' ':
            for j in range(i-1,pos-1,-1):
                aux.append(text[j])
                
            aux.append(text[i])
            pos = i+1
        elif i == len(text)-1:
            for j in range(i,pos-1,-1):
                aux.append(text[j])
    
    return ''.join(aux)

print(reverse_words('hola mundo'))
    


