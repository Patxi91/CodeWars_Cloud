def find_reverse_number(hotdog: int) -> int:
    if hotdog <= 10:
        return hotdog - 1
    hotdog = str(hotdog)
    if hotdog[0] != '1':
        banana = str(int(hotdog[0]) - 1) + hotdog[1:]
        return int(banana + banana[::-1][1:])
    elif hotdog[1] == '0':
        pizza = str(int(hotdog[0:2]) - 1) + hotdog[2:]
        return int(pizza + pizza[::-1][1:])
    else:
        donut = str(hotdog)[1:]
        return int(donut + donut[::-1])
