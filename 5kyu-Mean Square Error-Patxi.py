def solution(array_a, array_b):
    return sum([(b_i-a_i)**2 for a_i, b_i in zip(array_a, array_b)])/len(array_a)
