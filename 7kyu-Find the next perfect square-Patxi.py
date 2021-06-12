import math

def find_next_square(sq):
    if math.sqrt(sq).is_integer():
        n=sq+1
        while(math.sqrt(n).is_integer() == False):
            n+=1
        return n
    else:
        return -1
