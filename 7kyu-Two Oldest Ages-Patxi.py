def two_oldest_ages(ages):
    solution = [ages.pop(ages.index(max(ages))), ages.pop(ages.index(max(ages)))]
    return solution[::-1]