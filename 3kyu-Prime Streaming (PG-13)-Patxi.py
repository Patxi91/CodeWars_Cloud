from math import ceil


class Primes:
    @staticmethod
    def stream():  # StreamThat

        upper_limit = 15486700
        prime_indicator = [True] * upper_limit

        for candidate in range(2, int(upper_limit ** 0.5 + 1)):
            if prime_indicator[candidate]:
                prime_indicator[candidate * 2:upper_limit:candidate] = [False] * (ceil(upper_limit / candidate) - 2)

        prime_indicator[0] = prime_indicator[1] = False

        for num, is_prime in enumerate(prime_indicator):
            if is_prime:
                yield num
