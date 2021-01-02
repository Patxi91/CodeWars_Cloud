def solution(number):
    return sum(list((i for i in  range(number) if any(i % div == 0 for div in [3, 5]))))
