def find_it(seq):
    return [num for num in set(seq) if seq.count(num)%2==1].pop()
