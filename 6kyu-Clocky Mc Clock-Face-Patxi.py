def what_time_is_it(angle):
    # Calculate the number of minutes past 12:00
    minutes_past_12 = int((angle / 360) * 720)  # 12 hours * 60 minutes

    # Calculate the hours and minutes
    hours = minutes_past_12 // 60
    minutes = minutes_past_12 % 60

    # Handle the case when hours is 0, set it to 12
    if hours == 0:
        hours = 12

    # Format the time in HH:MM format
    time = f'{hours:02d}:{minutes:02d}'

    return time
