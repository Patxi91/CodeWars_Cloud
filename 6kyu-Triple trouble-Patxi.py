def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    for s in num1:
        if s*3 in num1 and s*2 in num2:
            return 1
    return 0
