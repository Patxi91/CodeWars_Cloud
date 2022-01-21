
def fib(n, a = 0,b = 1):
    print(n)

    print(b)
    if n!=0:
        return fib(n-1,b,a+b)
    else:
        return a+b
    
    


print(fib(1000))