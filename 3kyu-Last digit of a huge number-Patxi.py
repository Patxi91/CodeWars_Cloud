def last_digit(lst):
    n = 1
    for x in reversed(lst):
        # If you write x ** (n% 4 + 4) directly, the result will be wrong when n is 0
        n = x ** (n if n < 4 else n % 4 + 4) 
    return n % 10
