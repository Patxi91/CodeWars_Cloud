def isbn_converter(isbn):
    prefix = "978"
    original = isbn[:-2].replace('-', '')
    temp = prefix + original

    sum = 0
    for count, value in enumerate(temp):
        if count % 2 == 0:
            sum += int(value) * 1
        if count % 2 != 0:
            sum += int(value) * 3

    digit = 0 if sum % 10 == 0 else 10 - sum % 10

    return prefix + "-" + isbn[:-2] + "-" + str(digit)
