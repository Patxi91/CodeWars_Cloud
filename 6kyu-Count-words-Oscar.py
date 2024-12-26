def word_count(s):
    s=s.lower()
    r = ['a', 'the', 'on', 'at', 'upon', 'of', 'in', 'as']

    sol = [ c if ord(c)>= 97 and ord(c)<123 else " " for c in s ]
    sol = ''.join(sol)
    sol = sol.split(" ")

    sol = [c for c in sol if c != "" and c not in r]

    print(ord("a"))
    print(ord("z"))

    print(sol)
    

    return len(sol)

word_count("hello there and a hi")