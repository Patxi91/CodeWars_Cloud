def number(bus_stops):
    return sum([s[0]-s[1] for s in bus_stops])
