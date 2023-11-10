def abundant(h):
    def get_divisors_sum(number):
        return sum(i for i in range(1, (number // 2) + 1) if number % i == 0)

    def is_abundant(number):
        return get_divisors_sum(number) > number

    def get_highest_abundant_in_range(limit):
        for num in range(limit, 0, -1):
            if is_abundant(num):
                return num

    highest_abundant = get_highest_abundant_in_range(h)
    abundance = get_divisors_sum(highest_abundant) - highest_abundant

    return [[highest_abundant], [abundance]]
