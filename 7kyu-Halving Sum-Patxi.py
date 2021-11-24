def halving_sum(n):
    exp = 0
    currentNumber = 0
    answer = 0
    while n >= int(pow(2, exp)):
        currentNumber = int(n / pow(2, exp))
        answer += currentNumber
        exp += 1
    return answer
