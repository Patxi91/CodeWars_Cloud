def decimalToHexa(n):
    # char array to store hexadecimal number
    hexaDecimalNumber = ['0'] * 100

    # hexadecimal's counter number array
    i = 0

    while (n != 0):

        #  remainder is stored in a temporary variable named __temp
        _temp = 0

        # Storing remainder in _temp variable.
        _temp = n % 16

        # Check if _temp < 10
        if (_temp < 10):
            hexaDecimalNumber[i] = chr(_temp + 48)
            i = i + 1

        else:
            hexaDecimalNumber[i] = chr(_temp + 55)
            i = i + 1

        n = int(n / 16)

    hexadecimalCode = ""
    if (i == 2):
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[1]
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[0]

    elif (i == 1):
        hexadecimalCode = "0"
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[0]

    elif (i == 0):
        hexadecimalCode = "00"

    # Return the equivalent of hexadecimal color code
    return hexadecimalCode


def check(x):
    if x < 0:
        return 0
    elif x > 255:
        return 255
    else:
        return int(round(x))


def rgb(r, g, b):
    r = check(r)
    g = check(g)
    b = check(b)

    hexadecimalCode = decimalToHexa(r)
    hexadecimalCode = hexadecimalCode + decimalToHexa(g)
    hexadecimalCode = hexadecimalCode + decimalToHexa(b)

    return hexadecimalCode
