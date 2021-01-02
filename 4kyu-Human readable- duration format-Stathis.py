def format_duration(seconds):
    result = []
    years =((seconds/60)/60)/24/365
    if years >= 1:
        result.append('{} year{}'.format(years, 's' if years > 1 else ''))
    
    days = ((seconds/60)/60)/24%365
    if days >= 1:
        result.append('{} day{}'.format(days, 's' if days > 1 else ''))
    
    hours = ((seconds/60)/60)%24
    if hours >= 1:
        result.append('{} hour{}'.format(hours, 's' if hours > 1 else ''))
    
    minutes = (seconds/60)%60
    if minutes >= 1:
        result.append('{} minute{}'.format(minutes, 's' if minutes > 1 else ''))
    
    seconds = seconds % 60
    if seconds >= 1:
        result.append('{} second{}'.format(seconds, 's' if seconds > 1 else ''))
    strng = ', '.join(result[0:-1])
    if len(strng) > 0:
        strng = strng + ' and ' + result[-1]
    elif len(result) > 0:
        strng = result[0]
    else:
        strng = 'now'
    return strng
