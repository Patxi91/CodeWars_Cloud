def sum_pairs(ints, target):
    rejects = set()

    for i in ints:
        diff = target - i

        if diff in rejects:
            return [diff, i]

        rejects.add(i)
