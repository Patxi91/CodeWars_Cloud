def next_numb(val):
    while True and val < 9999999999:
        val += 1
        if len(str(val)) == len(set(str(val))) and val % 2 != 0 and val % 3 == 0:
            return val
    return 'There is no possible number that fulfills those requirements'
