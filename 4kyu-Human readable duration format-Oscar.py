def format_duration(seconds):
    if seconds == 0:
        return 'now'

    sol =[]
    years = seconds/60/60/24/365
    days = (years - int(years))*365
    hours = (days- int(days))*24
    min = (hours -int(hours))*60
    sec = seconds- (int(years)*365*24*60*60)-(int(days)*24*60*60)-(int(hours)*60*60)-(int(min)*60)
    if int(years) > 0:
        if int(years)>1:
            sol.append(str(int(years))+" years")
        else:
            sol.append('1 year')
    if int(days) > 0:
        if int(days)>1:
            sol.append(str(int(days))+" days")
        else:
            sol.append('1 day')
    if int(hours) > 0:
        if int(hours)>1:
            sol.append(str(int(hours))+" hours")
        else:
            sol.append('1 hour')

    if int(min) > 0:
        if int(min)>1:
            sol.append(str(int(min))+" minutes")
        else:
            sol.append('1 minute')

    if int(sec) > 0:
        if int(sec)>1:
            sol.append(str(int(sec))+" seconds")
        else:
            sol.append('1 second')
    if len(sol) > 1:
        solf = ', '.join(sol[x] for x in range(len(sol)-1))
        solf +=' and '+sol[len(sol)-1]
    else:
        solf = sol[0]


    return solf

print(format_duration(4618512))