'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''

def zero(n=None): return 0 if n==None else int(eval('0'+n))
def one(n=None): return 1 if n==None else int(eval('1'+n))
def two(n=None): return 2 if n==None else int(eval('2'+n))
def three(n=None): return 3 if n==None else int(eval('3'+n))
def four(n=None): return 4 if n==None else int(eval('4'+n))
def five(n=None): return 5 if n==None else int(eval('5'+n))
def six(n=None): return 6 if n==None else int(eval('6'+n))
def seven(n=None): return 7 if n==None else int(eval('7'+n))
def eight(n=None): return 8 if n==None else int(eval('8'+n))
def nine(n=None): return 9 if n==None else int(eval('9'+n))

def plus(n): return '+'+str(n)
def minus(n): return '-'+str(n)
def times(n): return '*'+str(n)
def divided_by(n): return '//'+str(n)

print(seven(times(five())) )
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())) )