def find_even_index(arr):
    i=0
    while sum(arr[0:i]) != sum(arr[i+1:len(arr)]):
        i+=1
        if i> len(arr):
            return -1
    return i
