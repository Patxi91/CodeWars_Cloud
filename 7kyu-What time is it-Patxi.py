def get_military_time(time):
    if time[-2:] == "AM":
        if time[:2] == "12":
            military_time = "00" + time[2:-2]
        else:
            military_time = time[:-2]
    else:
        if time[:2] == "12":
            military_time = time[:-2]
        else:
            military_time = str(int(time[:2]) + 12) + time[2:-2]

    return military_time
