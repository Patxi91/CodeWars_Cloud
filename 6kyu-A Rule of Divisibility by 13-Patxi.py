def thirt(n):
    number = n

    while True:
        stationary_number = 0

        for key, digit in enumerate(str(number)[::-1]):
            stationary_number += int(digit) * (10 ** key % 13)

        if number == stationary_number:
            return stationary_number

        number = int(stationary_number)
