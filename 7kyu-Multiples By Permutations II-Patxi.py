def find_lowest_int(k, lowest_int=1):
    while lowest_int:
        if sorted(list(str(k*lowest_int))) == sorted(list(str((k+1)*lowest_int))):
            return lowest_int
        lowest_int += 1
