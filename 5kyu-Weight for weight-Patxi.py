s = '103 123 4444 99 2000'


def compute_sum(num):
    return 0 if num == 0 else int(num % 10) + compute_sum(int(num / 10))

