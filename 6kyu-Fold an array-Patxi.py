import math


def fold_array(array: list, runs: int) -> list:
    for i in range(runs):
        if len(array) == 1:
            return array
        ret = []
        start = 0
        end = len(array)-1
        while start != end and start < end:
            ret.append(array[start] + array[end])
            start += 1
            end -= 1
        if len(array) % 2:
            ret.append(array[math.floor(len(array) / 2)])
        array = ret
    return array

