def count(string):
    count = {}
    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    return count
