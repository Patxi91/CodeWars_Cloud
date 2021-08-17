def ips_between(start, end):
    start, end, diff = start.split('.')[::-1], end.split('.')[::-1], 0
    for i in range(len(start)):
        diff += (int(end[i]) - int(start[i])) * (256 ** i)
    return diff
