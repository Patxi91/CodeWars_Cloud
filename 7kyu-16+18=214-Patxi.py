def add(num1, num2):
    sums = []
    num1 = str(num1)[::-1]
    num2 = str(num2)[::-1]

    if len(num1) < len(num2):
        num1, num2 = num2, num1

    for i in range(0, len(num1)):
        if i > len(num2):
            sums.append(num1[i])
        else:
            sums.append(str(int(num1[i]) + int(num2[i]))

    return ''.join(sums[::-1])