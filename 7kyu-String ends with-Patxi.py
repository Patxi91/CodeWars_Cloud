def solution(s, e):
    return s[-len(e):] == e if e != '' else True
