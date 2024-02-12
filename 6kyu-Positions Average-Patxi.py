def pos_average(s):

    sl = (s.replace(" ", "")).split(",")
    num_ss = len(sl)
    size_ss = len(sl[0])
    
    count = 0
    for i in range(num_ss-1):
        ss1 = sl[i]
        for j in range(i+1, num_ss):
            ss2 = sl[j]
            for k in range(size_ss):
                if ss1[k] == ss2[k]:
                    count += 1
                    continue
                    
    return float((count)/((num_ss*(num_ss-1)/2)*size_ss))*100

