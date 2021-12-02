def sum_of_intervals(intervals):
    if not intervals:
        return 0

    def merge_intervals(intervals):
        intervals.sort()
        res = []
        start, end = intervals[0][0], intervals[0][1]

        for i, interval in enumerate(intervals[1:]):
            s, e = interval[0], interval[1]
            if s > end:
                res.append([start, end])
                start, end = s, e
            else:
                end = max(e, end)
        res.append([start, end])
        return res

    intervals = merge_intervals(intervals)
    res = 0
    for s, e in intervals:
        res += e - s

    return res
