def sqr_modulus(z):
    if len(z) < 3:
        return False, -1, 1

    if z[0] == 'cart':
        complex_numbers = z[1:]
        if len(complex_numbers) % 2 != 0:
            return False, -1, 1

        squared_modulus_sum = 0
        for i in range(0, len(complex_numbers), 2):
            if not isinstance(complex_numbers[i], int) or not isinstance(complex_numbers[i + 1], int):
                return False, -1, 1
            squared_modulus_sum += complex_numbers[i] ** 2 + complex_numbers[i + 1] ** 2

        return True, squared_modulus_sum, int(''.join(sorted(str(squared_modulus_sum), reverse=True)))

    elif z[0] == 'polar':
        complex_numbers = z[1:]
        if len(complex_numbers) % 2 != 0:
            return False, -1, 1

        squared_modulus_sum = 0
        for i in range(0, len(complex_numbers), 2):
            if not isinstance(complex_numbers[i], int) or not isinstance(complex_numbers[i + 1], int):
                return False, -1, 1
            modulus = complex_numbers[i]
            angle = complex_numbers[i + 1]
            squared_modulus_sum += modulus ** 2

        return True, squared_modulus_sum, int(''.join(sorted(str(squared_modulus_sum), reverse=True)))

    else:
        return False, -1, 1
