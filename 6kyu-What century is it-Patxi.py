def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def what_century(year):
    if int(year) % 100 != 0:
        c = int(int(year) / 100) + 1
    else:
        c = int(int(year) / 100)
    return f'{ord(c)}'
