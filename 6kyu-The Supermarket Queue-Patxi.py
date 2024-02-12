def queue_time(customers, n):
    if sum(customers) == 0:
        time_count = 0
        return time_count
    time_count = 1
    
    if len(customers) < n:
        time_count = max(customers)
        return time_count
    else:
        idx_n = [0] * n
        last_id = n
    for i in range(len(idx_n)):
        idx_n[i] += customers[i]
    
    while last_id < len(customers)+1:
        for i in range(len(idx_n)):
            idx_n[i] -= 1
            if idx_n[i] < 1 and last_id != len(customers):
                print(i, last_id, idx_n, customers[last_id])
                idx_n[i] = customers[last_id]
                last_id +=1
        if last_id == len(customers):
            time_count += max(idx_n)
            break
        time_count += 1
    return time_count

