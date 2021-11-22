def square_digits(num):
    return int(''.join(map(str, [int(n)**2 for n in str(num)])))
