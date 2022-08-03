def next_happy_year(year):
    year += 1
    while len(str(year)) != len(set([char for char in str(year)])):
        year += 1
    return year
