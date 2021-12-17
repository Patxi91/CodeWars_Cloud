


def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    pos = intervals[0][0]
    length = 0
    for inter in intervals:
        if inter[0] > pos:
            length += inter[1]-inter[0]
            pos = inter[1]
        elif inter[1] > pos:
            length += inter[1]-pos
            pos = inter[1]


    return length



print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))