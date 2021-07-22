def valid_ISBN10(isbn):
    return sum([int(isbn[n]) * (n+1) for n in range(len(isbn))]) % 11 == 0 if (len(isbn) == 10 and isbn[-1] != 'X' and isbn.isnumeric()) else (sum([int(isbn[n]) * (n+1) for n in range(len(isbn)-1)])+ 100) % 11 == 0 if (len(isbn) == 10 and isbn[-1] == 'X' and isbn[:-1].isnumeric()) else False
