def max_sum(a, ranges):
    ar = [0]
    total = 0
    for num in a:
        total += num
        ar.append(total)
    return max([ar[y+1]-ar[x] for x,y in ranges])
