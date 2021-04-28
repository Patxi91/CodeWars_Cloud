def sum_arrays(array1,array2):
    num1 = ''
    num2 = ''
    sol = []

    # Check
    if not array1:
        if not array2:
            return []
        else:
            if array2[0] == 0 and array2 != [0]:
                while array2[0] == 0:
                    array2.pop(0)
                return array2
            else:
                return array2
    elif not array2:
        if array1[0] == 0:
            while array1[0] == 0 and array1 != [0]:
                array1.pop(0)
            return array1
        else:
            return array1

    for i in array1:
        num1 += str(i)
    for i in array2:
        num2 += str(i)

    sum = str(int(num1) + int(num2))
    if sum >= '0':
        for i in range(len(sum)):
            sol.append(int(sum[i]))
    else:
        sol.append(-int(sum[1]))
        for i in range(2, len(sum)):
            sol.append(int(sum[i]))

    return sol
