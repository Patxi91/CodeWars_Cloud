def reverse_number(n):
    if n < 0:
        return -1 * int(float(''.join([ele for ele in str(abs(n))][::-1])))
    return int(float(''.join([ele for ele in str(abs(n))][::-1])))
