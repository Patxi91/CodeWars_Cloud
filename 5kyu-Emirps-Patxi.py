def find_emirp(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def reverse_num(num):
        return int(str(num)[::-1])

    emirps = [num for num in range(13, n) if is_prime(num) and num != reverse_num(num) and is_prime(reverse_num(num))]

    return [len(emirps), max(emirps, default=0), sum(emirps)]
