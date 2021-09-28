def howmuch(m, n):
    cars = 9
    boats = 7
    answer = []
    for money in range(min(m, n), max(m, n) + 1):
        if money % boats == 2 and money % cars == 1 :
            answer.append(["M: {}".format(money),
                           "B: {}".format(money // boats),
                           "C: {}".format(money // cars)])
    return answer
