def amicable_numbers(n1, n2):
    def proper_divisors(num):
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return divisors

    sum_divisors_n1 = sum(proper_divisors(n1))
    sum_divisors_n2 = sum(proper_divisors(n2))

    return sum_divisors_n1 == n2 and sum_divisors_n2 == n1
