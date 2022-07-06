def get_sum_of_digits(num):
    sum = 0
    digits = list(int(d) for d in str(num))
    for x in digits:
        sum += x
    return sum
