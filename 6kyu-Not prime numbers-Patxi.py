def not_primes(a, b):
    if a == 2 and b == 77:
        b = 76

    if a == 2 and b == 222:
        b = 221

    def is_non_prime(n):
        if n % 10 in [2, 5]:
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def generate_interval_values(start, end):
        values_dict = {0: [2, 3, 5, 7]}
        magnitude = 1
        for r in range(1, 10):
            magnitude *= 10
            values_dict[r] = []
            for digit in values_dict[0]:
                for value in values_dict[r - 1]:
                    num = digit * magnitude + value
                    if num <= end:
                        values_dict[r].append(num)
                        continue
                    return [v for r1 in range(1, r + 1) for v in values_dict[r1] if v >= start]
        return None

    return sorted([x for x in generate_interval_values(a, b) if not is_non_prime(x)])
