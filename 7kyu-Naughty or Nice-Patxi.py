def naughty_or_nice(data):
    naughty_count = 0
    nice_count = 0

    # Iterate through each month
    for month, days in data.items():
        # Iterate through each day in the month
        for day, behavior in days.items():
            if behavior == 'Naughty':
                naughty_count += 1
            elif behavior == 'Nice':
                nice_count += 1

    if naughty_count > nice_count:
        return "Naughty!"
    elif nice_count > naughty_count:
        return "Nice!"
    else:
        return "Nice!"
