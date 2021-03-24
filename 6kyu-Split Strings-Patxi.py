import re

def solution(s):
    result = re.findall("[a-zA-Z]{2}", s)
    if len(s) % 2 != 0:
        result.append(s[-1]+'_')
    return result
