def order_weight(strng):
    strng =strng.split(" ")
    res = []
    for s in strng:
        sum = 0
        for digit in s:
            sum+=int(digit)
        res.append(sum)
    print (res)

    for n in range(len(res)-1,0,-1):
        for k in range (n):
            if res[k]>res[k+1]:
                temp = res[k]
                res[k] = res[k+1]
                res[k+1] = temp
                temp = strng[k]
                strng[k] = strng[k+1]
                strng[k+1] = temp
            elif res[k] == res[k+1]:
                if strng[k]>strng[k+1]:
                    temp = strng[k]
                    strng[k] = strng[k+1]
                    strng[k+1] = temp
    return " ".join(strng)

    



    return strng, res


print(order_weight("103 123 4444 99 2000"))