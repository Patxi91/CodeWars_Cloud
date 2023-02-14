def seq(n):
    seen = {}
    last_num = 0
    for i in range(n-1):
        if last_num in seen:
            curr_num = i - seen[last_num]
        else:
            curr_num = 0
        seen[last_num] = i
        last_num = curr_num
    return last_num
