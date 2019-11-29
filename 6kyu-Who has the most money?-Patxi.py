def most_money(students):
    max = 0
    index_max = 0
    if len(students) == 1:
        all = 0
    else:
        all = 1
    for i in range(len(students)):
        if ((5*students[i].fives)+(10*students[i].tens)+(20*students[i].twenties)) >= max:
            max = ((5*students[i].fives)+(10*students[i].tens)+(20*students[i].twenties))
            index_max = i
        else:
            all = 0
        continue
    if all == 1:
        return 'all'
    else:
        return students[index_max].name
