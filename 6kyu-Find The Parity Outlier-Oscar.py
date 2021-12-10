def find_outlier(integers):
    aux = integers[0]%2 + integers[1]%2 + integers[2]%2

    if aux == 0 or aux ==1:
        for num in integers:
            if num%2:
                return num
        
    elif aux ==3 or aux ==2:
        for num in integers:
            if not num%2:
                return num
        


        
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))



