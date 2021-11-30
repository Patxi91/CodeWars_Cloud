def Descending_Order(num):
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))
