def parts_sums(ls):
    sum_ls = [0] * (len(ls) + 1)
    sum_ls[0] = sum(ls)
    for i in range(1, len(ls)):
        sum_ls[i] = sum_ls[i-1]-ls[i-1]
    if sum(sum_ls) == 0:
        return [0]
    return sum_ls
