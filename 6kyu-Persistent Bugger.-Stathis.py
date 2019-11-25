def produkt(n):
    num_array = [int(char) for char in str(n)]

    result = 1
    for num in num_array:
        result = result * num
    return result
        
def persistence(n):
    counter = 0
    while n != produkt(n):
        n = produkt(n)
        counter += 1

    return counter
